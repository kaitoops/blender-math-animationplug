import os
import zipfile
import shutil
from pathlib import Path

def package_addon():
    """打包插件为zip文件"""
    # 获取当前目录
    current_dir = Path(__file__).parent
    addon_name = "blender-math-animationplug"
    version = "v12"
    
    # 创建临时目录
    temp_dir = current_dir / "temp_package"
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir()
    
    # 创建插件目录
    addon_dir = temp_dir / addon_name
    addon_dir.mkdir()
    
    # 需要包含的文件和目录
    include_items = [
        "__init__.py",
        "core",
        "objects",
        "animation",
        "render",
        "performance",
        "workflow",
        "mcp",
        "ui",
        "properties.py",
        "error_reporter.py",
        "README.md",
        "README_en.md",
        "LICENSE"
    ]
    
    # 复制文件和目录
    for item in include_items:
        src = current_dir / item
        dst = addon_dir / item
        if src.exists():
            if src.is_file():
                shutil.copy2(src, dst)
            else:
                shutil.copytree(src, dst)
    
    # 创建zip文件，使用版本号命名
    zip_path = current_dir / f"{addon_name}-{version}.zip"
    if zip_path.exists():
        zip_path.unlink()
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in addon_dir.rglob('*'):
            if file_path.is_file():
                arc_path = f"{addon_name}/{file_path.relative_to(addon_dir)}"
                zipf.write(file_path, arc_path)
    
    # 清理临时目录
    shutil.rmtree(temp_dir)
    
    print(f"插件已打包到: {zip_path}")
    return zip_path

if __name__ == "__main__":
    package_addon()