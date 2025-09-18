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
    # 检查依赖项 - 使用简化版检查
    try:
        from .core.dependency_checker_simple import DependencyChecker
        if not DependencyChecker.check_dependencies():
            print("警告: 依赖检查未完全通过，但将继续注册插件")
        else:
            print("✓ 依赖检查通过")
    except Exception as e:
        print(f"依赖检查出现错误，但将继续注册插件: {e}")
        
    # 注册属性
    properties.register()
    
    # 注册主面板（必须在UI面板之前注册）
    try:
        bpy.utils.register_class(MATH_ANIM_PT_main_panel)
        registered_classes.append(MATH_ANIM_PT_main_panel)
    except Exception as e:
        print(f"注册主面板失败: {e}")
        
    # 注册核心模块
    try:
        core.register()
    except Exception as e:
        print(f"注册核心模块失败: {e}")
    # 注册对象模块
    try:
        objects.register()
    except Exception as e:
        print(f"注册对象模块失败: {e}")
    # 注册动画模块
    try:
        animation.register()
    except Exception as e:
        print(f"注册动画模块失败: {e}")
    # 注册渲染模块
    try:
        render.register()
    except Exception as e:
        print(f"注册渲染模块失败: {e}")
    # 注册性能模块
    try:
        performance.register()
    except Exception as e:
        print(f"注册性能模块失败: {e}")
    # 注册工作流模块
    try:
        workflow.register()
    except Exception as e:
        print(f"注册工作流模块失败: {e}")
    # 注册MCP模块
    try:
        mcp.register()
    except Exception as e:
        print(f"注册MCP模块失败: {e}")
    
    # 注册UI面板（子面板）
    try:
        ui.register()
    except Exception as e:
        print(f"注册UI面板失败: {e}")
    
    # 注册错误报告工具
    try:
        bpy.utils.register_class(MATH_ANIM_OT_save_error_report)
        registered_classes.append(MATH_ANIM_OT_save_error_report)
    except Exception as e:
        print(f"注册错误报告工具失败: {e}")

def unregister():
    # 反注册错误报告工具
    if MATH_ANIM_OT_save_error_report in registered_classes:
        try:
            bpy.utils.unregister_class(MATH_ANIM_OT_save_error_report)
            registered_classes.remove(MATH_ANIM_OT_save_error_report)
        except Exception as e:
            print(f"注销错误报告工具失败: {e}")
    
    # 反注册UI面板（子面板）
    try:
        ui.unregister()
    except Exception as e:
        print(f"注销UI面板失败: {e}")
    
    # 反注册MCP模块
    try:
        mcp.unregister()
    except Exception as e:
        print(f"注销MCP模块失败: {e}")
    # 反注册工作流模块
    try:
        workflow.unregister()
    except Exception as e:
        print(f"注销工作流模块失败: {e}")
    # 反注册性能模块
    try:
        performance.unregister()
    except Exception as e:
        print(f"注销性能模块失败: {e}")
    # 反注册渲染模块
    try:
        render.unregister()
    except Exception as e:
        print(f"注销渲染模块失败: {e}")
    # 反注册动画模块
    try:
        animation.unregister()
    except Exception as e:
        print(f"注销动画模块失败: {e}")
    # 反注册对象模块
    try:
        objects.unregister()
    except Exception as e:
        print(f"注销对象模块失败: {e}")
    # 反注册核心模块
    try:
        core.unregister()
    except Exception as e:
        print(f"注销核心模块失败: {e}")
    
    # 反注册主面板
    if MATH_ANIM_PT_main_panel in registered_classes:
        try:
            bpy.utils.unregister_class(MATH_ANIM_PT_main_panel)
            registered_classes.remove(MATH_ANIM_PT_main_panel)
        except Exception as e:
            print(f"注销主面板失败: {e}")
        
    # 反注册属性
    try:
        properties.unregister()
    except Exception as e:
        print(f"注销属性失败: {e}")

if __name__ == "__main__":
    register()