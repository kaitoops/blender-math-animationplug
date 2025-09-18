import bpy
from bpy.props import PointerProperty
from .animation_controller import MCPAnimationController
from . import ui

def register():
    # MCPAnimationController已经在properties.py中作为属性组注册
    # 这里只需要注册UI组件
    ui.register()

def unregister():
    # 反注册UI组件
    try:
        ui.unregister()
    except Exception as e:
        print(f"注销MCP UI组件失败: {e}")