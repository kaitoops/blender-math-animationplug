# Blender数学动画插件完整安装指南

## 安装前准备

1. 确保已关闭Blender
2. 备份现有的Blender插件（如果需要）

## 清理旧版本

在安装新版本之前，建议清理旧版本的残留文件：

1. 运行Blender
2. 在Python控制台中执行以下代码：
```python
import bpy
bpy.ops.math_anim.cleanup_old_plugins()
```

或者运行[cleanup_residual_files.py](file:///G%3A/GitHubcodecollection/blender-math-animationplug/cleanup_residual_files.py)脚本。

## 安装新版本

1. 使用[package_plugin.py](file:///G%3A/GitHubcodecollection/blender-math-animationplug/package_plugin.py)打包插件：
   ```bash
   python package_plugin.py
   ```

2. 在Blender中安装插件：
   - 打开Blender
   - 进入 `编辑` > `偏好设置` > `插件`
   - 点击 `安装` 按钮
   - 选择生成的 `blender-math-animationplug-full.zip` 文件
   - 启用插件（勾选复选框）

## 验证安装

安装完成后，可以运行测试脚本验证插件是否正确安装：

1. 在Blender的Python控制台中运行：
```python
import bpy
bpy.ops.math_anim.test_fixes()
```

2. 查看信息区域的输出，确认所有测试都通过。

## 使用插件

安装成功后，可以在3D视图的右侧UI面板中找到"数学动画"选项卡，包含以下功能模块：

- 对象创建工具
- 动画工具
- 渲染与风格化
- 性能优化
- 工作流优化
- MCP控制器

## 常见问题解决

### 1. "Writing to ID classes in this context is not allowed" 错误

这是由于在UI面板的draw方法中直接修改属性导致的。新版本已修复此问题。

### 2. "property not found" 错误

这通常是由于属性未正确注册或访问路径不正确。确保使用了正确的属性访问路径：
```python
# 正确的访问方式
scene.math_anim_properties.render.material.preset

# 而不是
scene.math_anim_properties.material.preset
```

### 3. "unknown operator" 错误

这表示操作符未正确注册。确保所有操作符都在相应的__init__.py文件中正确注册。

## 故障排除

如果插件仍然无法正常工作：

1. 检查Blender的系统控制台是否有错误信息
2. 确认插件是否完全启用
3. 尝试重启Blender
4. 检查是否有其他插件冲突

## 更新日志

### v1.0.0
- 修复UI面板中的属性修改问题
- 确保所有操作符和属性正确注册
- 添加清理残留文件功能
- 改进错误处理和测试机制