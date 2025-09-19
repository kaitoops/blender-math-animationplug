import os
import zipfile

def package_plugin():
    """打包插件为ZIP文件，以便在Blender中安装"""
    
    # 定义插件名称和源目录
    plugin_name = "blender-math-animationplug-full"
    source_dir = os.path.dirname(os.path.abspath(__file__))
    output_zip = os.path.join(source_dir, f"{plugin_name}.zip")
    
    # 要排除的文件和目录
    exclude_items = {
        '.git', '__pycache__', '.gitignore', 'package_plugin.py', 
        'blender-math-animationplug-full.zip', 'test_fixes.py',
        'blender_test_fixes.py', 'reinstall_plugin_correctly.py',
        'FIXES_README.md', 'test_fixes_v2.py', 'FIXES_V2_README.md',
        'blender_cleanup_old_plugins.py', 'cleanup_old_plugins.py',
        'blender_test_registration.py', 'test_registration.py'
    }
    
    print(f"正在打包插件: {plugin_name}")
    print(f"源目录: {source_dir}")
    print(f"输出文件: {output_zip}")
    
    # 创建ZIP文件
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # 获取相对路径
            arc_root = os.path.relpath(root, source_dir)
            
            # 跳过要排除的目录
            dirs[:] = [d for d in dirs if d not in exclude_items]
            
            for file in files:
                # 跳过要排除的文件
                if file in exclude_items:
                    continue
                    
                # 构建文件的完整路径和在ZIP中的路径
                file_path = os.path.join(root, file)
                arc_path = os.path.join(plugin_name, arc_root, file) if arc_root != '.' else os.path.join(plugin_name, file)
                
                # 添加文件到ZIP
                zipf.write(file_path, arc_path)
                print(f"添加文件: {arc_path}")
    
    print(f"插件打包完成: {output_zip}")

if __name__ == "__main__":
    package_plugin()