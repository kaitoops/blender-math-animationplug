import os
import shutil
import zipfile

# Blender插件目录
blender_plugin_dir = os.path.expanduser("~/AppData/Roaming/Blender Foundation/Blender/4.5/scripts/addons")

# 插件源文件目录
plugin_source_dir = r"g:\GitHubcodecollection\blender-math-animationplug"
plugin_zip_path = r"g:\GitHubcodecollection\blender-math-animationplug\blender-math-animationplug-full-v7.zip"
plugin_folder_name = "blender-math-animationplug-full"

def remove_existing_plugin():
    """移除已存在的插件"""
    plugin_dirs = [
        os.path.join(blender_plugin_dir, plugin_folder_name),
        os.path.join(blender_plugin_dir, "blender-math-animationplug")
    ]
    
    for plugin_dir in plugin_dirs:
        if os.path.exists(plugin_dir):
            try:
                shutil.rmtree(plugin_dir)
                print(f"已移除已存在的插件目录: {plugin_dir}")
            except Exception as e:
                print(f"移除插件目录失败 {plugin_dir}: {e}")

def install_plugin():
    """安装插件"""
    try:
        # 移除已存在的插件
        remove_existing_plugin()
        
        # 创建临时目录来解压文件
        temp_dir = os.path.join(blender_plugin_dir, "temp_extract")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        
        # 解压插件到临时目录
        with zipfile.ZipFile(plugin_zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        # 移动插件目录到正确位置
        source_dir = os.path.join(temp_dir, "blender-math-animationplug")
        target_dir = os.path.join(blender_plugin_dir, plugin_folder_name)
        
        if os.path.exists(source_dir):
            shutil.move(source_dir, target_dir)
            print(f"插件已成功安装到: {target_dir}")
        else:
            # 如果没有找到blender-math-animationplug目录，直接移动整个临时目录
            shutil.move(temp_dir, target_dir)
            print(f"插件已成功安装到: {target_dir}")
        
        # 清理临时目录（如果还存在）
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        
        print("请在Blender中重新启动并启用插件")
        
    except Exception as e:
        print(f"安装插件失败: {e}")

if __name__ == "__main__":
    install_plugin()