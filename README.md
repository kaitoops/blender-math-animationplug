# Blender数学动画插件

## 简介

Blender数学动画插件是一个集成工具集，旨在帮助用户在Blender中创建高质量的数学动画内容。该插件提供了从基础数学对象创建到复杂动画制作的完整解决方案。

## 功能特性

### 核心功能模块

1. **数学对象创建**
   - 二维曲线绘制工具
   - 三维曲面生成器
   - 向量场可视化
   - 概率分布图表
   - LaTeX公式渲染
   - 坐标系构建器

2. **动画制作工具**
   - 路径绘制动画
   - 形状变形动画
   - 公式演变动画
   - 流体模拟动画
   - 几何变换动画

3. **渲染与风格化**
   - 材质预设系统
   - 灯光预设管理
   - NPR非真实感渲染
   - 特效应用系统
   - 风格切换器

4. **性能优化**
   - 实时预览优化
   - 网格简化工具
   - GPU加速支持
   - 批量导出功能

5. **工作流优化**
   - 模板系统
   - 公式编辑器
   - 交互式教程
   - 错误诊断工具

6. **MCP动画控制**
   - 动画控制器
   - 数据处理器
   - 渲染优化器
   - 工作流管理器

### 最新修复

- **插件模块化结构问题修复**：解决了插件被错误地解压为多个独立模块的问题，确保插件作为一个完整的单元正确安装
- **UI面板操作符属性设置问题修复**：解决了在UI面板中设置操作符属性时出现的AttributeError错误，确保公式编辑器能正常工作
- **模块注册问题修复**：解决了插件中"property not found"和"unknown operator"错误，确保所有属性和操作符能正确注册和访问
- **UI面板操作符属性访问问题修复**：解决了在UI面板中直接访问操作符实例属性导致的AttributeError错误，确保公式编辑器能正常工作
- **操作符属性缺失问题修复**：解决了ShowFormulaEditorOperator操作符缺少target_object_name属性的问题，确保公式编辑器能正常工作
- **MCPAnimationController初始化问题修复**：解决了访问MCP控制器时的初始化错误，确保MCP面板能正常显示和使用
- **循环导入问题修复**：解决了插件加载时的循环导入错误，确保插件能正常注册和使用
- **操作符名称一致性**：修复了UI面板中操作符调用名称不匹配的问题
- **方法名称一致性**：统一了操作符调用的方法名称
- **属性定义完善**：添加了缺失的属性定义，确保UI正常显示
- **属性访问修复**：修正了UI面板中的属性访问逻辑
- **V2版本修复**：解决了"Writing to ID classes in this context is not allowed"错误，通过修复UI面板中直接修改属性的问题，并确保所有操作符和属性正确注册

详细修复说明请查看 [FIXES_README.md](FIXES_README.md) 和 [FIXES_V2_README.md](FIXES_V2_README.md) 文件。

## 安装说明

1. 下载最新的插件ZIP文件：[blender-math-animationplug-full.zip](blender-math-animationplug-full.zip)
2. 打开Blender，进入 `编辑` → `首选项` → `插件`
3. 点击 `安装...` 按钮，选择下载的ZIP文件
4. 安装后勾选插件启用
5. 在3D视图中按 `N` 键打开右侧属性面板，选择"数学动画"选项卡

详细安装说明请查看 [INSTALL_INSTRUCTIONS.md](INSTALL_INSTRUCTIONS.md) 和 [COMPLETE_INSTALLATION_GUIDE.md](COMPLETE_INSTALLATION_GUIDE.md) 文件。

## 使用方法

1. 在3D视图的UI面板中找到"数学动画"选项卡
2. 根据需要选择相应的功能模块
3. 使用各模块提供的工具创建数学对象和动画
4. 应用渲染预设和风格化效果
5. 使用性能优化工具提高工作效率

## 依赖项

- Blender 3.0或更高版本
- Python 3.7或更高版本（随Blender提供）
- numpy (通过Blender内置Python环境)
- matplotlib (可选，用于高级图表功能)

## 文档

- [用户指南](docs/mcp_user_guide.md) - 面向最终用户的使用手册
- [开发者指南](docs/mcp_developer_guide.md) - 面向开发者的扩展开发文档
- [安装说明](INSTALL_INSTRUCTIONS.md) - 详细的安装和配置指南
- [修复说明](FIXES_README.md) - 插件问题修复记录
- [V2修复说明](FIXES_V2_README.md) - 最新问题修复记录
- [完整安装指南](COMPLETE_INSTALLATION_GUIDE.md) - 完整的安装和使用指南

## 贡献

欢迎提交Issue和Pull Request来改进这个插件。

## 许可证

本项目采用MIT许可证 - 详情请见 [LICENSE](LICENSE) 文件。

## 技术支持

如遇到问题，请：
1. 查看系统控制台的错误信息
2. 使用插件内的"保存错误报告"功能
3. 提交Issue到项目仓库