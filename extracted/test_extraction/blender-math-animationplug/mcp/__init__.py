import bpy
from bpy.props import PointerProperty
from .animation_controller import MCPAnimationController
from . import ui

def register():
    # 注册MCP动画控制器
    bpy.utils.register_class(MCPAnimationController)
    
    # 注册UI组件
    ui.register()

def unregister():
    # 反注册UI组件
    ui.unregister()
    
    # 反注册MCP动画控制器
    bpy.utils.unregister_class(MCPAnimationController)