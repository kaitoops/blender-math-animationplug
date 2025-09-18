bl_info = {
    "name": "Blender数学动画插件(核心版)",
    "author": "Gemini",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "3D视图 > UI面板 > 数学动画",
    "description": "一个用于创建数学动画的集成工具集(核心版)",
    "category": "Object",
}

import bpy

# 导入核心模块
from . import core
from . import properties

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
    print("注册数学动画插件(核心版)...")
    
    # 注册属性
    try:
        properties.register()
        print("✓ 属性注册成功")
    except Exception as e:
        print(f"✗ 属性注册失败: {e}")
        return
    
    # 注册主面板
    try:
        bpy.utils.register_class(MATH_ANIM_PT_main_panel)
        print("✓ 主面板注册成功")
    except Exception as e:
        print(f"✗ 主面板注册失败: {e}")
        return
    
    # 注册核心模块
    try:
        core.register()
        print("✓ 核心模块注册成功")
    except Exception as e:
        print(f"✗ 核心模块注册失败: {e}")

def unregister():
    print("注销数学动画插件(核心版)...")
    
    # 注销核心模块
    try:
        core.unregister()
        print("✓ 核心模块注销成功")
    except Exception as e:
        print(f"✗ 核心模块注销失败: {e}")
    
    # 注销主面板
    try:
        bpy.utils.unregister_class(MATH_ANIM_PT_main_panel)
        print("✓ 主面板注销成功")
    except Exception as e:
        print(f"✗ 主面板注销失败: {e}")
    
    # 注销属性
    try:
        properties.unregister()
        print("✓ 属性注销成功")
    except Exception as e:
        print(f"✗ 属性注销失败: {e}")

if __name__ == "__main__":
    register()