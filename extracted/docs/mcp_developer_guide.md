# MCP模块开发者文档

[English Version](mcp_developer_guide_en.md) | [中文版本](mcp_developer_guide.md)

## 架构概述

MCP（Motion Capture）模块采用模块化设计，主要包含以下核心组件：

1. **动画控制器** (MCPAnimationController)
   - 核心控制类，管理整个MCP功能的生命周期
   - 提供高级API接口
   - 协调其他组件的工作

2. **数据处理器** (MCPDataProcessor)
   - 处理MCP数据的加载和解析
   - 管理动画数据的格式转换
   - 提供数据优化功能

3. **工作流管理器** (MCPWorkflowManager)
   - 管理骨骼映射流程
   - 处理模板的保存和加载
   - 提供工作流程优化

4. **渲染优化器** (MCPRenderOptimizer)
   - 优化渲染性能
   - 管理视窗设置
   - 提供不同级别的性能优化

## 核心类API

### MCPAnimationController

```python
class MCPAnimationController(bpy.types.PropertyGroup):
    """MCP动画控制器类"""
    
    def load_animation(self, context):
        """加载MCP动画数据
        
        Args:
            context: Blender上下文对象
        
        Returns:
            bool: 加载是否成功
        """
        pass
    
    def apply_animation(self, context, armature):
        """应用MCP动画到骨骼装备
        
        Args:
            context: Blender上下文对象
            armature: 目标骨骼装备对象
        
        Returns:
            bool: 应用是否成功
        """
        pass
    
    def cleanup(self):
        """清理MCP动画数据和优化设置
        
        Returns:
            bool: 清理是否成功
        """
        pass
    
    def set_performance_level(self, level):
        """设置性能级别
        
        Args:
            level: PerformanceLevel枚举值
        """
        pass
```

### MCPDataProcessor

```python
class MCPDataProcessor:
    """MCP数据处理器类"""
    
    def load_mcp_file(self, file_path):
        """加载MCP文件
        
        Args:
            file_path: MCP文件路径
        
        Returns:
            bool: 加载是否成功
        """
        pass
    
    def get_animation_data(self):
        """获取动画数据
        
        Returns:
            dict: 处理后的动画数据
        """
        pass
    
    def apply_to_armature(self, armature, start_frame, end_frame,
                         smoothing_factor, auto_scale, processed_data):
        """应用动画数据到骨骼装备
        
        Args:
            armature: 目标骨骼装备
            start_frame: 起始帧
            end_frame: 结束帧
            smoothing_factor: 平滑系数
            auto_scale: 是否自动缩放
            processed_data: 预处理的动画数据
        
        Returns:
            bool: 应用是否成功
        """
        pass
```

### MCPWorkflowManager

```python
class MCPWorkflowManager:
    """MCP工作流管理器类"""
    
    def initialize_workflow(self, armature):
        """初始化工作流程
        
        Args:
            armature: 目标骨骼装备
        
        Returns:
            bool: 初始化是否成功
        """
        pass
    
    def save_mapping_template(self, template_name):
        """保存骨骼映射模板
        
        Args:
            template_name: 模板名称
        
        Returns:
            bool: 保存是否成功
        """
        pass
    
    def apply_mapping_template(self, template_name):
        """应用骨骼映射模板
        
        Args:
            template_name: 模板名称
        
        Returns:
            bool: 应用是否成功
        """
        pass
```

### MCPRenderOptimizer

```python
class MCPRenderOptimizer:
    """MCP渲染优化器类"""
    
    def setup_render_optimization(self, armature, performance_level):
        """设置渲染优化
        
        Args:
            armature: 目标骨骼装备
            performance_level: 性能级别
        """
        pass
    
    def optimize_viewport_performance(self):
        """优化视窗性能"""
        pass
    
    def optimize_render_settings(self, scene):
        """优化渲染设置
        
        Args:
            scene: Blender场景对象
        """
        pass
```

## 错误处理

所有模块都使用统一的错误处理机制：

```python
from ..core.error_handling import error_handler

@error_handler.performance_logged
def some_function():
    try:
        # 执行操作
        pass
    except Exception as e:
        error_handler.handle_object_error(e, "Operation description")
        return False
```

## 性能优化

性能优化分为三个级别：

```python
class PerformanceLevel(Enum):
    LOW = "low"      # 优先性能
    NORMAL = "normal" # 平衡模式
    HIGH = "high"    # 优先质量
```

## 开发指南

### 1. 代码风格

- 遵循PEP 8规范
- 使用类型注解
- 编写详细的文档字符串
- 保持代码模块化和可测试

### 2. 错误处理

- 使用统一的错误处理装饰器
- 提供有意义的错误信息
- 记录详细的错误日志

### 3. 性能优化

- 使用性能分析器监控关键操作
- 实现可配置的优化级别
- 优化内存使用和渲染性能

### 4. 测试

- 编写单元测试和集成测试
- 使用测试夹具模拟Blender环境
- 测试不同性能级别的行为

## 扩展开发

### 1. 添加新的数据格式支持

1. 在`MCPDataProcessor`中添加新的解析方法
2. 实现数据格式转换
3. 更新文档和测试

### 2. 自定义优化策略

1. 在`MCPRenderOptimizer`中添加新的优化方法
2. 实现不同性能级别的优化逻辑
3. 更新性能监控和日志

### 3. 扩展工作流程

1. 在`MCPWorkflowManager`中添加新的工作流程
2. 实现相关的UI控件
3. 更新文档和测试

## 版本控制

- 使用语义化版本号
- 维护更新日志
- 标记重要的API变更

## 调试技巧

1. 使用性能分析器定位瓶颈
2. 检查内存使用情况
3. 监控渲染性能指标
4. 分析错误日志