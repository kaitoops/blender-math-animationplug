import bpy
import time
import numpy as np
from ..core.error_handling import error_handler, PerformanceLevel

# 尝试导入psutil，如果不可用则使用基础性能监控
try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False
    error_handler.log_performance(
        PerformanceLevel.WARNING,
        "psutil未安装，将使用基础性能监控功能")


class PerformanceAnalyzer:
    """性能分析器，用于监控和优化插件性能"""
    
    def __init__(self):
        self.start_time = 0
        self.frame_times = []
        self.memory_usage = []
        self.performance_logs = []
        self.current_operation = None
    
    def start_monitoring(self, operation_name):
        """开始性能监控
        
        Args:
            operation_name: 操作名称
        """
        try:
            self.current_operation = operation_name
            self.start_time = time.time()
            self.frame_times.clear()
            self.memory_usage.clear()
            self.performance_logs.clear()
            
            # 记录初始内存使用
            self._record_memory_usage()
            
            return True
        except Exception as e:
            error_handler.handle_object_error(e, "Starting performance monitoring")
            return False
    
    def record_frame(self):
        """记录当前帧的性能数据"""
        try:
            if not self.current_operation:
                return False
            
            # 记录帧时间
            current_time = time.time()
            frame_time = current_time - self.start_time
            self.frame_times.append(frame_time)
            
            # 记录内存使用
            self._record_memory_usage()
            
            return True
        except Exception as e:
            error_handler.handle_object_error(e, "Recording frame performance")
            return False
    
    def _record_memory_usage(self):
        """记录当前内存使用情况"""
        try:
            if PSUTIL_AVAILABLE:
                # 确保psutil模块仍然可用
                try:
                    process = psutil.Process()
                    memory_info = process.memory_info()
                    self.memory_usage.append(memory_info.rss)
                except Exception:
                    # 如果psutil在运行时出现问题，回退到基础模式
                    self.memory_usage.append(-1)
            else:
                # 如果psutil不可用，记录一个占位值
                self.memory_usage.append(-1)
        except Exception as e:
            # 确保即使在记录内存使用时出错也不会导致整个函数失败
            self.memory_usage.append(-1)
    
    def analyze_performance(self):
        """分析性能数据
        
        Returns:
            dict: 性能分析结果
        """
        try:
            if not self.current_operation:
                return None
            
            # 计算帧时间统计
            frame_times = np.array(self.frame_times)
            frame_stats = {
                'avg_frame_time': np.mean(frame_times),
                'max_frame_time': np.max(frame_times),
                'min_frame_time': np.min(frame_times),
                'std_frame_time': np.std(frame_times)
            }
            
            # 计算内存使用统计
            memory_usage = np.array(self.memory_usage)
            if PSUTIL_AVAILABLE and len(memory_usage) > 0 and memory_usage[0] != -1:
                memory_stats = {
                    'avg_memory': np.mean(memory_usage) / (1024 * 1024),  # MB
                    'max_memory': np.max(memory_usage) / (1024 * 1024),    # MB
                    'min_memory': np.min(memory_usage) / (1024 * 1024),    # MB
                    'memory_growth': (memory_usage[-1] - memory_usage[0]) / (1024 * 1024)  # MB
                }
            else:
                memory_stats = {
                    'avg_memory': -1,
                    'max_memory': -1,
                    'min_memory': -1,
                    'memory_growth': -1,
                    'note': 'psutil未安装，内存监控不可用'
                }
            
            # 生成性能报告
            report = {
                'operation': self.current_operation,
                'total_time': time.time() - self.start_time,
                'frame_count': len(self.frame_times),
                'frame_stats': frame_stats,
                'memory_stats': memory_stats,
                'performance_logs': self.performance_logs
            }
            
            return report
        except Exception as e:
            error_handler.handle_object_error(e, "Analyzing performance")
            return None
    
    def optimize_performance(self, context, performance_level=PerformanceLevel.NORMAL):
        """根据性能分析结果优化性能
        
        Args:
            context: Blender上下文
            performance_level: 性能级别
        """
        try:
            report = self.analyze_performance()
            if not report:
                return False
            
            # 根据性能报告调整设置
            if report['frame_stats']['avg_frame_time'] > 0.1:  # 帧时间过长
                self._optimize_frame_performance(context, performance_level)
            
            # 只有在psutil可用且内存监控有效时才进行内存优化
            if (PSUTIL_AVAILABLE and 
                report['memory_stats']['memory_growth'] > 100):  # 内存增长超过100MB
                self._optimize_memory_usage(context, performance_level)
            
            return True
        except Exception as e:
            error_handler.handle_object_error(e, "Optimizing performance")
            return False
    
    def _optimize_frame_performance(self, context, performance_level):
        """优化帧性能
        
        Args:
            context: Blender上下文
            performance_level: 性能级别
        """
        try:
            # 调整视窗设置
            space = context.space_data
            if space and space.type == 'VIEW_3D':
                # 根据性能级别调整显示选项
                if performance_level == PerformanceLevel.HIGH:
                    space.show_gizmo = False
                    space.overlay.show_overlays = False
                    space.shading.type = 'SOLID'
                elif performance_level == PerformanceLevel.NORMAL:
                    space.show_gizmo = True
                    space.overlay.show_overlays = True
                    space.shading.type = 'SOLID'
                else:
                    space.show_gizmo = True
                    space.overlay.show_overlays = True
                    space.shading.type = 'MATERIAL'
            
            # 记录优化操作
            self.performance_logs.append({
                'type': 'frame_optimization',
                'level': performance_level.name,
                'timestamp': time.time()
            })
        except Exception as e:
            error_handler.handle_object_error(e, "Optimizing frame performance")
    
    def _optimize_memory_usage(self, context, performance_level):
        """优化内存使用
        
        Args:
            context: Blender上下文
            performance_level: 性能级别
        """
        try:
            # 清理未使用的数据块
            bpy.ops.outliner.orphans_purge(do_recursive=True)
            
            # 根据性能级别调整内存相关设置
            if performance_level == PerformanceLevel.HIGH:
                # 最大限度减少内存使用
                context.scene.render.use_persistent_data = False
                context.scene.render.use_save_buffers = False
            elif performance_level == PerformanceLevel.NORMAL:
                # 平衡内存使用和性能
                context.scene.render.use_persistent_data = True
                context.scene.render.use_save_buffers = False
            else:
                # 优先考虑功能完整性
                context.scene.render.use_persistent_data = True
                context.scene.render.use_save_buffers = True
            
            # 记录优化操作
            self.performance_logs.append({
                'type': 'memory_optimization',
                'level': performance_level.name,
                'timestamp': time.time()
            })
        except Exception as e:
            error_handler.handle_object_error(e, "Optimizing memory usage")
    
    def stop_monitoring(self):
        """停止性能监控并生成报告"""
        try:
            if not self.current_operation:
                return None
            
            # 生成最终报告
            report = self.analyze_performance()
            
            # 清理状态
            self.current_operation = None
            self.start_time = 0
            self.frame_times.clear()
            self.memory_usage.clear()
            self.performance_logs.clear()
            
            return report
        except Exception as e:
            error_handler.handle_object_error(e, "Stopping performance monitoring")
            return None