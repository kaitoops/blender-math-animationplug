import bpy
import traceback

class ErrorDiagnostic(bpy.types.PropertyGroup):
    """错误诊断工具，用于捕获和报告插件运行中的错误"""
    
    def run_with_diagnostic(self, func, *args, **kwargs):
        """在错误诊断上下文中运行函数"""
        try:
            return func(*args, **kwargs)
        except Exception as e:
            self.report_error(e)
            return None

    def report_error(self, error):
        """报告错误，可以在UI中显示"""
        error_message = f"错误: {str(error)}\n"
        error_message += "详细信息:\n"
        error_message += traceback.format_exc()
        
        print(error_message) # 打印到控制台
        
        # 在Blender UI中显示一个错误报告
        def draw_error(self, context):
            self.layout.label(text=f"插件发生错误: {str(error)}")
            self.layout.label(text="详情请查看系统控制台")
            
        bpy.context.window_manager.popup_menu(draw_error, title="数学动画插件错误", icon='ERROR')