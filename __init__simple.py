bl_info = {
    "name": "Blender数学动画插件(简化版)",
    "author": "Gemini",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "3D视图 > UI面板 > 数学动画",
    "description": "一个用于创建数学动画的集成工具集(简化版)",
    "category": "Object",
}

import bpy

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
    print("注册数学动画插件...")
    try:
        bpy.utils.register_class(MATH_ANIM_PT_main_panel)
        print("✓ 主面板注册成功")
    except Exception as e:
        print(f"✗ 主面板注册失败: {e}")

def unregister():
    print("注销数学动画插件...")
    try:
        bpy.utils.unregister_class(MATH_ANIM_PT_main_panel)
        print("✓ 主面板注销成功")
    except Exception as e:
        print(f"✗ 主面板注销失败: {e}")

if __name__ == "__main__":
    register()