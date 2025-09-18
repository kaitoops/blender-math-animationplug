# Blender数学动画插件安装说明

## 插件包信息
- **插件名称**: Blender数学动画插件
- **版本**: 1.0.0
- **打包日期**: 2025-09-19
- **打包文件**: blender-math-animationplug-full.zip

## 安装步骤

### 方法一：通过Blender界面安装（推荐）

1. 打开Blender
2. 进入 `编辑` → `首选项`
3. 点击 `插件` 选项卡
4. 点击 `安装...` 按钮
5. 浏览并选择 `blender-math-animationplug-full.zip` 文件
6. 点击 `安装插件`
7. 在插件列表中找到 "Blender数学动画插件"
8. 勾选插件名称前的复选框以启用插件

### 方法二：手动安装

1. 关闭Blender
2. 解压 `blender-math-animationplug-full.zip` 文件
3. 将解压后的 `blender-math-animationplug-full` 文件夹复制到Blender的插件目录：
   - **Windows**: `C:\Users\[用户名]\AppData\Roaming\Blender Foundation\Blender\[版本号]\scripts\addons\`
   - **macOS**: `/Users/[用户名]/Library/Application Support/Blender/[版本号]/scripts/addons/`
   - **Linux**: `/home/[用户名]/.config/blender/[版本号]/scripts/addons/`
4. 启动Blender
5. 进入 `编辑` → `首选项` → `插件`
6. 搜索 "数学动画" 或 "Math Animation"
7. 勾选插件名称前的复选框以启用插件

## 验证安装

安装成功后，您应该能在3D视图的UI面板中看到"数学动画"选项卡，其中包含以下功能模块：
- 对象创建工具
- 动画制作工具
- 渲染与风格化
- 性能优化
- 工作流优化
- MCP动画控制

## 常见问题

### 1. 插件无法启用
- 确保Blender版本为3.0或更高版本
- 检查插件是否完整解压到addons目录
- 查看系统控制台是否有错误信息

### 2. 面板不显示
- 确保插件已正确启用
- 在3D视图中按 `N` 键打开右侧属性面板
- 选择"数学动画"选项卡

### 3. 功能异常
- 检查是否有依赖库缺失
- 查看Blender系统控制台的错误信息
- 确认插件版本与Blender版本兼容

## 卸载插件

### 通过Blender界面卸载
1. 进入 `编辑` → `首选项` → `插件`
2. 找到 "Blender数学动画插件"
3. 点击插件条目右侧的 `删除` 按钮
4. 确认删除操作

### 手动卸载
1. 关闭Blender
2. 删除Blender插件目录中的 `blender-math-animationplug-full` 文件夹
3. 重启Blender

## 技术支持

如遇到问题，请查看以下资源：
- 错误报告：使用插件内的"保存错误报告"功能
- 文档：查看 `docs` 文件夹中的用户指南和开发者文档
- GitHub：访问项目仓库获取最新更新和支持