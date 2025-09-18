import bpy
import traceback
import os

class ErrorReporter:
    """错误报告工具类"""
    
    @staticmethod
    def get_error_log():
        """获取当前错误日志"""
        try:
            # 获取系统信息
            import tempfile
            temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt')
            temp_file.close()
            
            # 保存系统信息到临时文件
            bpy.ops.wm.sysinfo(filepath=temp_file.name)
            
            # 读取临时文件内容
            with open(temp_file.name, 'r', encoding='utf-8') as f:
                log_content = f.read()
            
            # 删除临时文件
            os.unlink(temp_file.name)
            
            return log_content
        except Exception as e:
            return f"无法获取系统信息: {str(e)}"
    
    @staticmethod
    def save_error_report(filepath):
        """保存错误报告到文件"""
        try:
            log_content = ErrorReporter.get_error_log()
            
            # 添加当前时间戳
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            report_content = f"Blender 数学动画插件错误报告\n"
            report_content += f"生成时间: {timestamp}\n"
            report_content += "=" * 50 + "\n\n"
            report_content += log_content
            
            # 保存到文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            return True
        except Exception as e:
            print(f"保存错误报告失败: {str(e)}")
            return False

def register():
    """注册错误报告操作"""
    pass

def unregister():
    """注销错误报告操作"""
    pass

if __name__ == "__main__":
    # 测试代码
    pass