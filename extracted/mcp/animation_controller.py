import bpy
import numpy as np
from ..core.error_handling import error_handler, PerformanceLevel, ObjectError
from .render_optimizer import MCPRenderOptimizer
from bpy.props import StringProperty, IntProperty, FloatProperty, BoolProperty
from .workflow_manager import MCPWorkflowManager
from ..core.performance import PerformanceAnalyzer

class MCPAnimationController(bpy.types.PropertyGroup):
    """MCP动画控制器，用于管理和应用动作捕捉动画"""
    
    # 属性定义
    mcp_file: StringProperty(
        name="MCP文件",
        description="选择MCP动作捕捉数据文件",
        default="",
        subtype='FILE_PATH'
    )
    
    start_frame: IntProperty(
        name="起始帧",
        description="动画起始帧",
        default=1,
        min=0
    )
    
    end_frame: IntProperty(
        name="结束帧",
        description="动画结束帧",
        default=250,
        min=1
    )
    
    smoothing_factor: FloatProperty(
        name="平滑系数",
        description="动画平滑程度",
        default=0.5,
        min=0.0,
        max=1.0
    )
    
    auto_scale: BoolProperty(
        name="自动缩放",
        description="自动调整动画比例",
        default=True
    )
    
    mapping_template: StringProperty(
        name="映射模板",
        description="选择骨骼映射模板",
        default=""
    )
    
    def __init__(self):
        super().__init__()
        self._data_processor = None
        self._render_optimizer = MCPRenderOptimizer()
        self._workflow_manager = MCPWorkflowManager()
        self._performance_analyzer = PerformanceAnalyzer()
        self._performance_level = PerformanceLevel.NORMAL
    
    def load_animation(self, context):
        """加载MCP动画数据"""
        try:
            # 开始性能监控
            self._performance_analyzer.start_monitoring("Loading MCP Animation")
            
            if not self.mcp_file:
                raise ValueError("未选择MCP文件")
            
            # 初始化数据处理器
            from .data_processor import MCPDataProcessor
            self._data_processor = MCPDataProcessor()
            
            # 加载动画数据
            success = self._data_processor.load_mcp_file(self.mcp_file)
            if not success:
                raise RuntimeError("加载MCP文件失败")
            
            # 分析性能并优化
            self._performance_analyzer.optimize_performance(context, self._performance_level)
            
            # 停止性能监控
            report = self._performance_analyzer.stop_monitoring()
            if report:
                error_handler.log_performance(
                    PerformanceLevel.INFO,
                    f"MCP动画加载性能报告: {report}"
                )
            
            return True
        except Exception as e:
            error_handler.handle_object_error(e, "Loading MCP animation")
            return False
    
    def apply_animation(self, context, armature):
        """应用MCP动画到骨骼装备"""
        try:
            # 开始性能监控
            self._performance_analyzer.start_monitoring("Applying MCP Animation")
            
            if not self._data_processor:
                raise RuntimeError("未加载MCP数据")
            
            # 初始化工作流程
            if not self._workflow_manager.initialize_workflow(armature):
                raise RuntimeError("初始化工作流程失败")
            
            # 应用骨骼映射模板
            if self.mapping_template:
                if not self._workflow_manager.apply_mapping_template(self.mapping_template):
                    raise RuntimeError("应用骨骼映射模板失败")
            
            # 预处理动画数据
            processed_data = self._workflow_manager.preprocess_animation_data(
                self._data_processor.get_animation_data()
            )
            if not processed_data:
                raise RuntimeError("预处理动画数据失败")
            
            # 设置渲染优化
            self._render_optimizer.setup_render_optimization(
                armature,
                self._performance_level
            )
            
            # 优化视窗性能
            self._render_optimizer.optimize_viewport_performance()
            
            # 优化渲染设置
            self._render_optimizer.optimize_render_settings(context.scene)
            
            # 应用动画数据
            success = self._data_processor.apply_to_armature(
                armature,
                self.start_frame,
                self.end_frame,
                self.smoothing_factor,
                self.auto_scale,
                processed_data
            )
            
            if not success:
                self._render_optimizer.restore_original_settings()
                raise RuntimeError("应用动画失败")
            
            # 记录每帧性能数据
            for frame in range(self.start_frame, self.end_frame + 1):
                context.scene.frame_set(frame)
                self._performance_analyzer.record_frame()
            
            # 分析性能并优化
            self._performance_analyzer.optimize_performance(context, self._performance_level)
            
            # 停止性能监控
            report = self._performance_analyzer.stop_monitoring()
            if report:
                error_handler.log_performance(
                    PerformanceLevel.INFO,
                    f"MCP动画应用性能报告: {report}"
                )
            
            return True
        except Exception as e:
            error_handler.handle_object_error(e, "Applying MCP animation")
            return False
    
    def cleanup(self):
        """清理MCP动画数据和优化设置"""
        try:
            # 开始性能监控
            self._performance_analyzer.start_monitoring("Cleaning up MCP Animation")
            
            # 清理数据处理器
            if self._data_processor:
                self._data_processor.cleanup()
                self._data_processor = None
            
            # 清理工作流程
            self._workflow_manager.cleanup_workflow()
            
            # 恢复渲染设置
            self._render_optimizer.restore_original_settings()
            
            # 停止性能监控
            report = self._performance_analyzer.stop_monitoring()
            if report:
                error_handler.log_performance(
                    PerformanceLevel.INFO,
                    f"MCP动画清理性能报告: {report}"
                )
            
            return True
        except Exception as e:
            error_handler.handle_object_error(e, "Cleaning up MCP animation")
            return False
    
    def set_performance_level(self, level):
        """设置性能级别
        
        Args:
            level: PerformanceLevel枚举值
        """
        self._performance_level = level
    
    def save_mapping_template(self, template_name):
        """保存当前骨骼映射为模板
        
        Args:
            template_name: 模板名称
        """
        return self._workflow_manager.save_mapping_template(template_name)