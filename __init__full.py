bl_info = {
    "name": "Blender数学动画插件(完整版)",
    "author": "Gemini",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "3D视图 > UI面板 > 数学动画",
    "description": "一个用于创建数学动画的集成工具集(完整版)",
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
from . import error_reporter
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

# --- 错误报告操作 ---

class MATH_ANIM_OT_save_error_report(bpy.types.Operator):
    """保存错误报告操作"""
    bl_idname = "math_anim.save_error_report"
    bl_label = "保存错误报告"
    bl_description = "保存当前错误日志到文件"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filename_ext = ".txt"

    def execute(self, context):
        if error_reporter.ErrorReporter.save_error_report(self.filepath):
            self.report({'INFO'}, f"错误报告已保存到: {self.filepath}")
        else:
            self.report({'ERROR'}, "保存错误报告失败")
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

# --- 注册与反注册 ---

# 跟踪已注册的类
registered_classes = []

def register():
    print("注册数学动画插件(完整版)...")
    
    # 检查依赖项
    try:
        from .core.dependency_checker import DependencyChecker
        if not DependencyChecker.check_dependencies():
            print("依赖检查失败")
            return
        print("✓ 依赖检查通过")
    except Exception as e:
        print(f"✗ 依赖检查失败: {e}")
        return
    
    # 注册属性
    try:
        properties.register()
        print("✓ 属性注册成功")
    except Exception as e:
        print(f"✗ 属性注册失败: {e}")
        return
    
    # 注册主面板（必须在UI面板之前注册）
    try:
        bpy.utils.register_class(MATH_ANIM_PT_main_panel)
        registered_classes.append(MATH_ANIM_PT_main_panel)
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
    
    # 注册对象模块
    try:
        objects.register()
        print("✓ 对象模块注册成功")
    except Exception as e:
        print(f"✗ 对象模块注册失败: {e}")
    
    # 注册动画模块
    try:
        animation.register()
        print("✓ 动画模块注册成功")
    except Exception as e:
        print(f"✗ 动画模块注册失败: {e}")
    
    # 注册渲染模块
    try:
        render.register()
        print("✓ 渲染模块注册成功")
    except Exception as e:
        print(f"✗ 渲染模块注册失败: {e}")
    
    # 注册性能模块
    try:
        performance.register()
        print("✓ 性能模块注册成功")
    except Exception as e:
        print(f"✗ 性能模块注册失败: {e}")
    
    # 注册工作流模块
    try:
        workflow.register()
        print("✓ 工作流模块注册成功")
    except Exception as e:
        print(f"✗ 工作流模块注册失败: {e}")
    
    # 注册MCP模块
    try:
        mcp.register()
        print("✓ MCP模块注册成功")
    except Exception as e:
        print(f"✗ MCP模块注册失败: {e}")
    
    # 注册UI面板（子面板）
    try:
        ui.register()
        print("✓ UI面板注册成功")
    except Exception as e:
        print(f"✗ UI面板注册失败: {e}")
    
    # 注册错误报告工具
    try:
        bpy.utils.register_class(MATH_ANIM_OT_save_error_report)
        registered_classes.append(MATH_ANIM_OT_save_error_report)
        print("✓ 错误报告工具注册成功")
    except Exception as e:
        print(f"✗ 错误报告工具注册失败: {e}")

def unregister():
    print("注销数学动画插件(完整版)...")
    
    # 反注册错误报告工具
    if MATH_ANIM_OT_save_error_report in registered_classes:
        try:
            bpy.utils.unregister_class(MATH_ANIM_OT_save_error_report)
            registered_classes.remove(MATH_ANIM_OT_save_error_report)
            print("✓ 错误报告工具注销成功")
        except Exception as e:
            print(f"✗ 错误报告工具注销失败: {e}")
    
    # 反注册UI面板（子面板）
    try:
        ui.unregister()
        print("✓ UI面板注销成功")
    except Exception as e:
        print(f"✗ UI面板注销失败: {e}")
    
    # 反注册MCP模块
    try:
        mcp.unregister()
        print("✓ MCP模块注销成功")
    except Exception as e:
        print(f"✗ MCP模块注销失败: {e}")
    
    # 反注册工作流模块
    try:
        workflow.unregister()
        print("✓ 工作流模块注销成功")
    except Exception as e:
        print(f"✗ 工作流模块注销失败: {e}")
    
    # 反注册性能模块
    try:
        performance.unregister()
        print("✓ 性能模块注销成功")
    except Exception as e:
        print(f"✗ 性能模块注销失败: {e}")
    
    # 反注册渲染模块
    try:
        render.unregister()
        print("✓ 渲染模块注销成功")
    except Exception as e:
        print(f"✗ 渲染模块注销失败: {e}")
    
    # 反注册动画模块
    try:
        animation.unregister()
        print("✓ 动画模块注销成功")
    except Exception as e:
        print(f"✗ 动画模块注销失败: {e}")
    
    # 反注册对象模块
    try:
        objects.unregister()
        print("✓ 对象模块注销成功")
    except Exception as e:
        print(f"✗ 对象模块注销失败: {e}")
    
    # 反注册核心模块
    try:
        core.unregister()
        print("✓ 核心模块注销成功")
    except Exception as e:
        print(f"✗ 核心模块注销失败: {e}")
    
    # 反注册主面板
    if MATH_ANIM_PT_main_panel in registered_classes:
        try:
            bpy.utils.unregister_class(MATH_ANIM_PT_main_panel)
            registered_classes.remove(MATH_ANIM_PT_main_panel)
            print("✓ 主面板注销成功")
        except Exception as e:
            print(f"✗ 主面板注销失败: {e}")
    
    # 反注册属性
    try:
        properties.unregister()
        print("✓ 属性注销成功")
    except Exception as e:
        print(f"✗ 属性注销失败: {e}")

if __name__ == "__main__":
    register()