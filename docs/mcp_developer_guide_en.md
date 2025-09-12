# MCP Module Developer Documentation

[English Version](mcp_developer_guide_en.md) | [中文版本](mcp_developer_guide.md)

## Architecture Overview

The MCP (Motion Capture) module adopts a modular design, mainly including the following core components:

1. **Animation Controller** (MCPAnimationController)
   - Core control class, managing the lifecycle of the entire MCP functionality
   - Provides high-level API interfaces
   - Coordinates the work of other components

2. **Data Processor** (MCPDataProcessor)
   - Processes loading and parsing of MCP data
   - Manages format conversion of animation data
   - Provides data optimization functions

3. **Workflow Manager** (MCPWorkflowManager)
   - Manages bone mapping workflow
   - Handles saving and loading of templates
   - Provides workflow optimization

4. **Render Optimizer** (MCPRenderOptimizer)
   - Optimizes rendering performance
   - Manages viewport settings
   - Provides different levels of performance optimization

## Core Class API

### MCPAnimationController

```python
class MCPAnimationController(bpy.types.PropertyGroup):
    """MCP Animation Controller Class"""
    
    def load_animation(self, context):
        """Load MCP animation data
        
        Args:
            context: Blender context object
        
        Returns:
            bool: Whether loading was successful
        """
        pass
    
    def apply_animation(self, context, armature):
        """Apply MCP animation to bone rig
        
        Args:
            context: Blender context object
            armature: Target bone rig object
        
        Returns:
            bool: Whether application was successful
        """
        pass
    
    def cleanup(self):
        """Clean up MCP animation data and optimization settings
        
        Returns:
            bool: Whether cleanup was successful
        """
        pass
    
    def set_performance_level(self, level):
        """Set performance level
        
        Args:
            level: PerformanceLevel enum value
        """
        pass
```

### MCPDataProcessor

```python
class MCPDataProcessor:
    """MCP Data Processor Class"""
    
    def load_mcp_file(self, file_path):
        """Load MCP file
        
        Args:
            file_path: MCP file path
        
        Returns:
            bool: Whether loading was successful
        """
        pass
    
    def get_animation_data(self):
        """Get animation data
        
        Returns:
            dict: Processed animation data
        """
        pass
    
    def apply_to_armature(self, armature, start_frame, end_frame,
                         smoothing_factor, auto_scale, processed_data):
        """Apply animation data to bone rig
        
        Args:
            armature: Target bone rig
            start_frame: Start frame
            end_frame: End frame
            smoothing_factor: Smoothing coefficient
            auto_scale: Whether to auto scale
            processed_data: Preprocessed animation data
        
        Returns:
            bool: Whether application was successful
        """
        pass
```

### MCPWorkflowManager

```python
class MCPWorkflowManager:
    """MCP Workflow Manager Class"""
    
    def initialize_workflow(self, armature):
        """Initialize workflow
        
        Args:
            armature: Target bone rig
        
        Returns:
            bool: Whether initialization was successful
        """
        pass
    
    def save_mapping_template(self, template_name):
        """Save bone mapping template
        
        Args:
            template_name: Template name
        
        Returns:
            bool: Whether saving was successful
        """
        pass
    
    def apply_mapping_template(self, template_name):
        """Apply bone mapping template
        
        Args:
            template_name: Template name
        
        Returns:
            bool: Whether application was successful
        """
        pass
```

### MCPRenderOptimizer

```python
class MCPRenderOptimizer:
    """MCP Render Optimizer Class"""
    
    def setup_render_optimization(self, armature, performance_level):
        """Set up render optimization
        
        Args:
            armature: Target bone rig
            performance_level: Performance level
        """
        pass
    
    def optimize_viewport_performance(self):
        """Optimize viewport performance"""
        pass
    
    def optimize_render_settings(self, scene):
        """Optimize render settings
        
        Args:
            scene: Blender scene object
        """
        pass
```

## Error Handling

All modules use a unified error handling mechanism:

```python
from ..core.error_handling import error_handler

@error_handler.performance_logged
def some_function():
    try:
        # Execute operation
        pass
    except Exception as e:
        error_handler.handle_object_error(e, "Operation description")
        return False
```

## Performance Optimization

Performance optimization is divided into three levels:

```python
class PerformanceLevel(Enum):
    LOW = "low"      # Prioritize performance
    NORMAL = "normal" # Balanced mode
    HIGH = "high"    # Prioritize quality
```

## Development Guide

### 1. Code Style

- Follow PEP 8 specifications
- Use type annotations
- Write detailed docstrings
- Keep code modular and testable

### 2. Error Handling

- Use unified error handling decorators
- Provide meaningful error messages
- Record detailed error logs

### 3. Performance Optimization

- Use performance profiler to monitor critical operations
- Implement configurable optimization levels
- Optimize memory usage and rendering performance

### 4. Testing

- Write unit tests and integration tests
- Use test fixtures to simulate Blender environment
- Test behavior at different performance levels

## Extension Development

### 1. Adding New Data Format Support

1. Add new parsing methods in `MCPDataProcessor`
2. Implement data format conversion
3. Update documentation and tests

### 2. Custom Optimization Strategies

1. Add new optimization methods in `MCPRenderOptimizer`
2. Implement optimization logic for different performance levels
3. Update performance monitoring and logging

### 3. Extending Workflow

1. Add new workflows in `MCPWorkflowManager`
2. Implement related UI controls
3. Update documentation and tests

## Version Control

- Use semantic versioning
- Maintain changelog
- Mark important API changes

## Debugging Tips

1. Use performance profiler to locate bottlenecks
2. Check memory usage
3. Monitor rendering performance metrics
4. Analyze error logs