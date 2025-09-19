# Blender数学动画插件安装说明

## 安装步骤

1. 下载插件ZIP文件: `blender-math-animationplug-full-clean.zip`

2. 打开Blender

3. 进入 `编辑` → `偏好设置` → `插件` 选项卡

4. 点击 `安装...` 按钮

5. 选择下载的ZIP文件

6. 找到"Blender数学动画插件"并启用它

7. 保存用户设置

## 验证安装

安装完成后，你应该能在3D视图的右侧UI面板中看到"数学动画"选项卡。

## 测试修复

安装后，可以运行测试操作符来验证修复是否成功：

1. 在Blender中按 `F3` 打开搜索菜单
2. 搜索 "Test Plugin Fixes"
3. 运行 "Math Anim: Test Plugin Fixes" 操作符
4. 查看信息区域的输出结果

## 重新安装

如果需要重新安装插件，请运行 `reinstall_plugin_correctly.py` 脚本。
