bl_info = {
    "name": "Blender数学动画插件",
    "author": "Gemini",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "3D视图 > UI面板 > 数学动画",
    "description": "一个用于创建数学动画的集成工具集",
    "category": "Object",
}

import bpy

# 导入所有模块
from . import core
from . import objects
from . import animation
from . import render
from . import performance
from . import workflow
from . import mcp
from . import ui

# --- UI 面板定义 ---

class MATH_ANIM_PT_main_panel(bpy.types.Panel):
    """主UI面板"""
    bl_label = "数学动画工具集"
    bl_idname = "MATH_ANIM_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '数学动画'

    def draw(self, context):
        layout = self.layout
        layout.label(text="欢迎使用数学动画插件!")


# --- 注册与反注册 ---

def register():
    # 注册核心模块
    core.register()
    # 注册对象模块
    objects.register()
    # 注册动画模块
    animation.register()
    # 注册渲染模块
    render.register()
    # 注册性能模块
    performance.register()
    # 注册工作流模块
    workflow.register()
    # 注册MCP模块
    mcp.register()
    
    # 注册UI
    ui.register()

def unregister():
    # 反注册UI
    ui.unregister()
        
    # 反注册MCP模块
    mcp.unregister()
    # 反注册工作流模块
    workflow.unregister()
    # 反注册性能模块
    performance.unregister()
    # 反注册渲染模块
    render.unregister()
    # 反注册动画模块
    animation.unregister()
    # 反注册对象模块
    objects.unregister()
    # 反注册核心模块
    core.unregister()

if __name__ == "__main__":
    register()