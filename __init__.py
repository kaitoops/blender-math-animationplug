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
import os
import shutil

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
        # 延迟导入error_reporter模块以避免循环导入
        from . import error_reporter
        if error_reporter.ErrorReporter.save_error_report(self.filepath):
            self.report({'INFO'}, f"错误报告已保存到: {self.filepath}")
        else:
            self.report({'ERROR'}, "保存错误报告失败")
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

# --- 测试修复操作 ---

class MATH_ANIM_OT_test_fixes(bpy.types.Operator):
    """测试插件修复是否正确的操作符"""
    bl_idname = "math_anim.test_fixes"
    bl_label = "Test Plugin Fixes"
    
    def execute(self, context):
        self.test_plugin_registration()
        return {'FINISHED'}
        
    def test_plugin_registration(self):
        """测试插件注册是否正确"""
        try:
            # 检查主属性组是否存在
            if hasattr(bpy.types.Scene, 'math_anim_properties'):
                print("✓ 主属性组已注册")
                self.report({'INFO'}, "主属性组已注册")
            else:
                print("✗ 主属性组未注册")
                self.report({'ERROR'}, "主属性组未注册")
                
            # 检查性能模块属性
            scene = context.scene
            if hasattr(scene, 'math_anim_properties'):
                perf_props = scene.math_anim_properties.performance
                if hasattr(perf_props, 'realtime_preview'):
                    print("✓ RealtimePreview属性已注册")
                    self.report({'INFO'}, "RealtimePreview属性已注册")
                    # 检查属性是否存在
                    if hasattr(perf_props.realtime_preview, 'use_simplify'):
                        print("✓ use_simplify属性存在")
                        self.report({'INFO'}, "use_simplify属性存在")
                    else:
                        print("✗ use_simplify属性不存在")
                        self.report({'ERROR'}, "use_simplify属性不存在")
                        
                    if hasattr(perf_props.realtime_preview, 'display_mode'):
                        print("✓ display_mode属性存在")
                        self.report({'INFO'}, "display_mode属性存在")
                    else:
                        print("✗ display_mode属性不存在")
                        self.report({'ERROR'}, "display_mode属性不存在")
                else:
                    print("✗ RealtimePreview属性未注册")
                    self.report({'ERROR'}, "RealtimePreview属性未注册")
                    
                if hasattr(perf_props, 'mesh_simplification'):
                    print("✓ MeshSimplification属性已注册")
                    self.report({'INFO'}, "MeshSimplification属性已注册")
                else:
                    print("✗ MeshSimplification属性未注册")
                    self.report({'ERROR'}, "MeshSimplification属性未注册")
                    
                if hasattr(perf_props, 'gpu_acceleration'):
                    print("✓ GPUAcceleration属性已注册")
                    self.report({'INFO'}, "GPUAcceleration属性已注册")
                else:
                    print("✗ GPUAcceleration属性未注册")
                    self.report({'ERROR'}, "GPUAcceleration属性未注册")
                    
                if hasattr(perf_props, 'batch_export'):
                    print("✓ BatchExport属性已注册")
                    self.report({'INFO'}, "BatchExport属性已注册")
                else:
                    print("✗ BatchExport属性未注册")
                    self.report({'ERROR'}, "BatchExport属性未注册")
            else:
                print("✗ math_anim_properties不存在")
                self.report({'ERROR'}, "math_anim_properties不存在")
                
            # 检查工作流模块属性
            if hasattr(scene, 'math_anim_properties'):
                wf_props = scene.math_anim_properties.workflow
                if hasattr(wf_props, 'templates'):
                    print("✓ TemplateManager属性已注册")
                    self.report({'INFO'}, "TemplateManager属性已注册")
                else:
                    print("✗ TemplateManager属性未注册")
                    self.report({'ERROR'}, "TemplateManager属性未注册")
                    
                if hasattr(wf_props, 'formula_editor'):
                    print("✓ FormulaEditor属性已注册")
                    self.report({'INFO'}, "FormulaEditor属性已注册")
                    # 检查属性是否存在
                    if hasattr(wf_props.formula_editor, 'formula_text'):
                        print("✓ formula_text属性存在")
                        self.report({'INFO'}, "formula_text属性存在")
                    else:
                        print("✗ formula_text属性不存在")
                        self.report({'ERROR'}, "formula_text属性不存在")
                        
                    if hasattr(wf_props.formula_editor, 'target_object_name'):
                        print("✓ target_object_name属性存在")
                        self.report({'INFO'}, "target_object_name属性存在")
                    else:
                        print("✗ target_object_name属性不存在")
                        self.report({'ERROR'}, "target_object_name属性不存在")
                else:
                    print("✗ FormulaEditor属性未注册")
                    self.report({'ERROR'}, "FormulaEditor属性未注册")
                    
            # 检查操作符是否注册
            try:
                # 尝试访问性能模块操作符
                bpy.ops.math_anim.apply_realtime_preview
                print("✓ apply_realtime_preview操作符已注册")
                self.report({'INFO'}, "apply_realtime_preview操作符已注册")
            except:
                print("✗ apply_realtime_preview操作符未注册")
                self.report({'ERROR'}, "apply_realtime_preview操作符未注册")
                
            try:
                bpy.ops.math_anim.apply_mesh_simplification
                print("✓ apply_mesh_simplification操作符已注册")
                self.report({'INFO'}, "apply_mesh_simplification操作符已注册")
            except:
                print("✗ apply_mesh_simplification操作符未注册")
                self.report({'ERROR'}, "apply_mesh_simplification操作符未注册")
                
            try:
                bpy.ops.math_anim.apply_gpu_acceleration
                print("✓ apply_gpu_acceleration操作符已注册")
                self.report({'INFO'}, "apply_gpu_acceleration操作符已注册")
            except:
                print("✗ apply_gpu_acceleration操作符未注册")
                self.report({'ERROR'}, "apply_gpu_acceleration操作符未注册")
                
            try:
                bpy.ops.math_anim.batch_export
                print("✓ batch_export操作符已注册")
                self.report({'INFO'}, "batch_export操作符已注册")
            except:
                print("✗ batch_export操作符未注册")
                self.report({'ERROR'}, "batch_export操作符未注册")
                
            try:
                bpy.ops.math_anim.apply_template
                print("✓ apply_template操作符已注册")
                self.report({'INFO'}, "apply_template操作符已注册")
            except:
                print("✗ apply_template操作符未注册")
                self.report({'ERROR'}, "apply_template操作符未注册")
                
            try:
                bpy.ops.math_anim.show_formula_editor
                print("✓ show_formula_editor操作符已注册")
                self.report({'INFO'}, "show_formula_editor操作符已注册")
            except:
                print("✗ show_formula_editor操作符未注册")
                self.report({'ERROR'}, "show_formula_editor操作符未注册")
                
        except Exception as e:
            print(f"测试过程中出现错误: {e}")
            self.report({'ERROR'}, f"测试过程中出现错误: {e}")
            
        return {'FINISHED'}

# --- 清理操作 ---

class MATH_ANIM_OT_cleanup_old_plugins(bpy.types.Operator):
    """清理旧插件残留文件操作符"""
    bl_idname = "math_anim.cleanup_old_plugins"
    bl_label = "Cleanup Old Plugins"
    
    def execute(self, context):
        try:
            # 获取插件路径
            addon_path = bpy.utils.user_resource('SCRIPTS', "addons")
            
            self.report({'INFO'}, f"插件目录: {addon_path}")
            
            # 清理残留的Python文件
            residual_files = [
                "properties.py",
                "error_reporter.py",
                "package_addon.py",
                "package_full_addon.py",
                "__init__.py",
                "LICENSE",
                "README.md",
                "README_en.md"
            ]
            
            for file_name in residual_files:
                file_path = os.path.join(addon_path, file_name)
                if os.path.exists(file_path):
                    try:
                        os.remove(file_path)
                        self.report({'INFO'}, f"已删除残留文件: {file_name}")
                    except Exception as e:
                        self.report({'ERROR'}, f"删除文件 {file_name} 时出错: {e}")
            
            # 清理残留的目录
            residual_dirs = [
                "blender-math-animationplug-full",
                "blender-mcp-main",
                "blender-math-animationplug",
                "blender-math-animationplug-core",
                "blender-math-animationplug-objects",
                "blender-math-animationplug-extracted"
            ]
            
            for dir_name in residual_dirs:
                dir_path = os.path.join(addon_path, dir_name)
                if os.path.exists(dir_path):
                    try:
                        shutil.rmtree(dir_path)
                        self.report({'INFO'}, f"已删除残留目录: {dir_name}")
                    except Exception as e:
                        self.report({'ERROR'}, f"删除目录 {dir_name} 时出错: {e}")
            
            self.report({'INFO'}, "清理完成!")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"清理过程中出错: {e}")
            return {'CANCELLED'}

# --- 注册与反注册 ---

# 跟踪已注册的类
registered_classes = []

# 导入所有模块（放在操作符定义之后以避免循环导入）
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
        
    # 注册测试操作符
    try:
        bpy.utils.register_class(MATH_ANIM_OT_test_fixes)
        registered_classes.append(MATH_ANIM_OT_test_fixes)
    except Exception as e:
        print(f"注册测试操作符失败: {e}")
        
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
        
    # 注册清理操作符
    try:
        bpy.utils.register_class(MATH_ANIM_OT_cleanup_old_plugins)
        registered_classes.append(MATH_ANIM_OT_cleanup_old_plugins)
    except Exception as e:
        print(f"注册清理操作符失败: {e}")

def unregister():
    # 反注册清理操作符
    if MATH_ANIM_OT_cleanup_old_plugins in registered_classes:
        try:
            bpy.utils.unregister_class(MATH_ANIM_OT_cleanup_old_plugins)
            registered_classes.remove(MATH_ANIM_OT_cleanup_old_plugins)
        except Exception as e:
            print(f"注销清理操作符失败: {e}")
    
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
            
    # 反注册测试操作符
    if MATH_ANIM_OT_test_fixes in registered_classes:
        try:
            bpy.utils.unregister_class(MATH_ANIM_OT_test_fixes)
            registered_classes.remove(MATH_ANIM_OT_test_fixes)
        except Exception as e:
            print(f"注销测试操作符失败: {e}")
        
    # 反注册属性
    try:
        properties.unregister()
    except Exception as e:
        print(f"注销属性失败: {e}")

if __name__ == "__main__":
    register()
