import os
import zipfile
from pathlib import Path

def validate_plugin_structure():
    """验证插件结构"""
    plugin_dir = Path(".")
    
    print("验证插件目录结构...")
    print("=" * 50)
    
    # 检查必需的文件和目录
    required_items = [
        "__init__.py",
        "core",
        "ui",
        "objects",
        "animation",
        "render",
        "performance",
        "workflow",
        "mcp",
        "properties.py",
        "error_reporter.py",
        "README.md",
        "LICENSE"
    ]
    
    missing_items = []
    for item in required_items:
        item_path = plugin_dir / item
        if not item_path.exists():
            missing_items.append(item)
    
    if missing_items:
        print("缺失的项目:")
        for item in missing_items:
            print(f"  - {item}")
        return False
    else:
        print("✓ 所有必需的文件和目录都存在")
    
    # 检查各模块的__init__.py文件
    modules = ["core", "ui", "objects", "animation", "render", "performance", "workflow", "mcp"]
    for module in modules:
        init_file = plugin_dir / module / "__init__.py"
        if not init_file.exists():
            print(f"✗ {module}模块缺少__init__.py文件")
            return False
        else:
            print(f"✓ {module}模块__init__.py文件存在")
    
    # 检查UI模块的面板文件
    ui_panels = [
        "object_panel.py",
        "animation_panel.py", 
        "render_panel.py",
        "performance_panel.py",
        "workflow_panel.py"
    ]
    
    for panel in ui_panels:
        panel_file = plugin_dir / "ui" / panel
        if not panel_file.exists():
            print(f"✗ UI模块缺少{panel}文件")
            return False
        else:
            print(f"✓ UI模块{panel}文件存在")
    
    print("=" * 50)
    print("插件结构验证通过!")
    return True

def validate_zip_contents():
    """验证ZIP文件内容"""
    zip_path = Path("blender-math-animationplug-v12.zip")
    
    if not zip_path.exists():
        print("ZIP文件不存在")
        return False
    
    print("验证ZIP文件内容...")
    print("=" * 50)
    
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        files = [f.filename for f in zipf.filelist]
    
    # 检查根目录
    root_dirs = set()
    for file_path in files:
        parts = file_path.split('/')
        if len(parts) > 1 and parts[0]:
            root_dirs.add(parts[0])
    
    if len(root_dirs) != 1:
        print("✗ ZIP文件应该只有一个根目录")
        return False
    
    plugin_dir_name = list(root_dirs)[0]
    if plugin_dir_name != "blender-math-animationplug":
        print(f"✗ 插件目录名应该是'blender-math-animationplug'，实际是'{plugin_dir_name}'")
        return False
    
    print(f"✓ 插件目录名正确: {plugin_dir_name}")
    
    # 检查必需的文件
    required_files = [
        f"{plugin_dir_name}/__init__.py",
        f"{plugin_dir_name}/properties.py",
        f"{plugin_dir_name}/error_reporter.py",
        f"{plugin_dir_name}/README.md",
        f"{plugin_dir_name}/LICENSE"
    ]
    
    for req_file in required_files:
        if req_file not in files:
            print(f"✗ 缺少必需文件: {req_file}")
            return False
        else:
            print(f"✓ 必需文件存在: {req_file}")
    
    # 检查模块目录
    modules = ["core", "ui", "objects", "animation", "render", "performance", "workflow", "mcp"]
    for module in modules:
        module_dir = f"{plugin_dir_name}/{module}/"
        if not any(f.startswith(module_dir) for f in files):
            print(f"✗ 缺少模块目录: {module}")
            return False
        else:
            print(f"✓ 模块目录存在: {module}")
    
    # 检查UI面板文件
    ui_panels = [
        "object_panel.py",
        "animation_panel.py", 
        "render_panel.py",
        "performance_panel.py",
        "workflow_panel.py"
    ]
    
    for panel in ui_panels:
        panel_file = f"{plugin_dir_name}/ui/{panel}"
        if panel_file not in files:
            print(f"✗ 缺少UI面板文件: {panel}")
            return False
        else:
            print(f"✓ UI面板文件存在: {panel}")
    
    print("=" * 50)
    print("ZIP文件内容验证通过!")
    return True

if __name__ == "__main__":
    print("插件验证工具")
    print("=" * 50)
    
    # 验证当前目录结构
    structure_ok = validate_plugin_structure()
    print()
    
    # 验证ZIP文件
    zip_ok = validate_zip_contents()
    print()
    
    if structure_ok and zip_ok:
        print("✓ 所有验证通过，插件可以正常工作")
    else:
        print("✗ 存在验证错误，请检查上述问题")