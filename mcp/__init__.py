import bpy
from bpy.props import PointerProperty
from .animation_controller import MCPAnimationController
from . import ui

def register():
    # 注册MCP动画控制器
    bpy.utils.register_class(MCPAnimationController)
    
    # 将MCP控制器添加到场景属性
    if not hasattr(bpy.types.Scene.math_anim_properties, "mcp"):
        bpy.types.Scene.math_anim_properties.mcp = PointerProperty(
            type=MCPAnimationController,
            name="MCP Animation Controller"
        )
    
    # 注册UI组件
    ui.register()

def unregister():
    # 反注册UI组件
    ui.unregister()
    
    # 移除场景属性
    if hasattr(bpy.types.Scene.math_anim_properties, "mcp"):
        del bpy.types.Scene.math_anim_properties.mcp
    
    # 反注册MCP动画控制器
    bpy.utils.unregister_class(MCPAnimationController)