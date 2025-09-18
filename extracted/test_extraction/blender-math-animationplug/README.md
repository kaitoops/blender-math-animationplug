# Blender数学动画插件

[English Version](README_en.md) | [中文版本](README.md)

## 项目简介

这是一个专为Blender设计的数学动画插件，旨在简化数学概念的可视化和动画制作过程。该插件提供了丰富的工具和功能，帮助用户创建高质量的数学教育内容和科学可视化作品。

## 主要功能

### 1. 基础数学对象
- 2D/3D坐标系统
- 向量场可视化
- 概率分布图形
- LaTeX公式渲染
- 曲线和曲面绘制

### 2. 动画系统
- 公式演化动画
- 形态变换效果
- 路径绘制动画
- 流体动画效果
- 动作捕捉(MCP)支持

### 3. 渲染功能
- 材质系统
- 照明控制
- 非真实感渲染
- 特殊效果
- 风格切换器

### 4. 性能优化
- GPU加速
- 网格简化
- 实时预览
- 批量导出

### 5. 工作流程
- 公式编辑器
- 交互式教程
- 错误诊断
- 模板系统

## 安装说明

### 方法一：使用打包好的zip文件安装（推荐）
1. 下载最新版本的插件压缩包 [blender-math-animationplug.zip](blender-math-animationplug.zip)
2. 在Blender中打开首选项（Edit > Preferences）
3. 点击"Add-ons"选项卡
4. 点击"Install..."按钮
5. 选择下载的插件压缩包
6. 启用插件（勾选复选框）

### 方法二：手动打包安装
1. 克隆或下载本仓库到本地
2. 运行打包脚本生成zip文件：
   ```bash
   python package_addon.py
   ```
3. 按照方法一的步骤安装生成的zip文件

### 方法三：开发模式安装
1. 克隆本仓库到本地
2. 在Blender的插件设置中，点击"Install..."按钮
3. 选择仓库根目录下的[__init__.py](file:///G:/GitHubcodecollection/blender-math-animationplug/__init__.py)文件
4. 启用插件

## 故障排除

### 常见问题及解决方案

1. **插件无法启用，提示循环导入错误**
   - 确保使用的是最新版本的插件
   - 删除Blender插件目录中的旧版本插件
   - 重新安装插件

2. **插件启用后UI面板不显示**
   - 检查Blender的3D视图右侧的UI面板是否已展开
   - 查看"数学动画"选项卡是否在UI面板中显示

3. **缺少依赖模块（如psutil）**
   - 插件会自动检测依赖项并在缺少时给出提示
   - 按照提示安装所需的Python包

4. **LaTeX公式渲染问题**
   - 确保系统已安装LaTeX发行版（如TeX Live或MiKTeX）
   - 检查插件设置中的LaTeX路径配置

## 使用要求

- Blender 3.0或更高版本
- Python 3.7或更高版本
- 建议使用支持GPU的显卡以获得最佳性能

## 文档

- [用户指南 (中文)](docs/mcp_user_guide.md) | [User Guide (English)](docs/mcp_user_guide_en.md)
- [开发者文档 (中文)](docs/mcp_developer_guide.md) | [Developer Documentation (English)](docs/mcp_developer_guide_en.md)

## 贡献指南

欢迎提交问题报告和功能建议！如果您想为项目做出贡献：

1. Fork本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m '添加一些特性'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个Pull Request

## 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

```
MIT License

Copyright (c) 2024 [作者名称]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```