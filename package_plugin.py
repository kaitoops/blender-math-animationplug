import os
import zipfile
import shutil
from pathlib import Path
import datetime

def package_plugin():
    """打包插件为Blender可安装的ZIP格式"""
    
    # 源代码路径
    source_dir = "g:/GitHubcodecollection/blender-math-animationplug"
    # 临时目录
    temp_dir = "g:/GitHubcodecollection/blender-math-animationplug-temp"
    # 输出ZIP文件路径
    output_zip = "g:/GitHubcodecollection/blender-math-animationplug-full.zip"
    
    print("开始打包Blender数学动画插件...")
    
    # 清理临时目录（如果存在）
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        print("清理临时目录...")
    
    # 创建临时目录
    os.makedirs(temp_dir, exist_ok=True)
    
    # 创建插件根目录
    plugin_dir = os.path.join(temp_dir, "blender-math-animationplug-full")
    os.makedirs(plugin_dir, exist_ok=True)
    
    # 需要复制的文件和目录列表
    items_to_copy = [
        "__init__.py",
        "properties.py",
        "error_reporter.py",
        "reinstall_plugin.py",
        "test_fixes.py",
        "FIXES_README.md",
        "INSTALL_INSTRUCTIONS.md",
        "README.md",
        "LICENSE",
        "core",
        "objects",
        "animation",
        "render",
        "performance",
        "workflow",
        "mcp",
        "ui",
        "docs"
    ]
    
    # 复制文件和目录
    for item in items_to_copy:
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(plugin_dir, item)
        
        if os.path.isfile(source_path):
            shutil.copy2(source_path, dest_path)
            print(f"复制文件: {item}")
        elif os.path.isdir(source_path):
            shutil.copytree(source_path, dest_path)
            print(f"复制目录: {item}")
        else:
            print(f"警告: {item} 不存在，跳过")
    
    # 创建ZIP文件
    print("创建ZIP文件...")
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arc_path = os.path.relpath(file_path, temp_dir)
                zipf.write(file_path, arc_path)
                print(f"添加到ZIP: {arc_path}")
    
    # 清理临时目录
    shutil.rmtree(temp_dir)
    print("清理临时目录...")
    
    # 更新INSTALL_INSTRUCTIONS.md中的打包日期
    update_install_instructions()
    
    print(f"插件打包完成: {output_zip}")
    print("您可以将此ZIP文件直接在Blender中安装")

def update_install_instructions():
    """更新安装说明中的打包日期"""
    install_instructions_path = "g:/GitHubcodecollection/blender-math-animationplug/INSTALL_INSTRUCTIONS.md"
    
    if os.path.exists(install_instructions_path):
        # 读取文件内容
        with open(install_instructions_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 获取当前日期
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # 更新打包日期
        import re
        updated_content = re.sub(
            r"(\*\*打包日期\*\*: )\d{4}-\d{2}-\d{2}", 
            f"**打包日期**: {current_date}", 
            content
        )
        
        # 写回文件
        with open(install_instructions_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"更新安装说明中的打包日期为: {current_date}")

if __name__ == "__main__":
    package_plugin()