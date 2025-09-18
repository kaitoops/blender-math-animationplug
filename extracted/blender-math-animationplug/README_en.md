# Blender Math Animation Plugin

[English Version](README_en.md) | [中文版本](README.md)

## Project Introduction

This is a mathematics animation plugin designed specifically for Blender, aimed at simplifying the visualization and animation process of mathematical concepts. The plugin provides rich tools and features to help users create high-quality mathematical educational content and scientific visualization works.

## Main Features

### 1. Basic Mathematical Objects
- 2D/3D Coordinate Systems
- Vector Field Visualization
- Probability Distribution Graphs
- LaTeX Formula Rendering
- Curve and Surface Drawing

### 2. Animation System
- Formula Evolution Animation
- Morphing Effects
- Path Drawing Animation
- Fluid Animation Effects
- Motion Capture (MCP) Support

### 3. Rendering Features
- Material System
- Lighting Control
- Non-Photorealistic Rendering
- Special Effects
- Style Switcher

### 4. Performance Optimization
- GPU Acceleration
- Mesh Simplification
- Real-time Preview
- Batch Export

### 5. Workflow
- Formula Editor
- Interactive Tutorials
- Error Diagnosis
- Template System

## Installation Instructions

### Method 1: Install using packaged zip file (Recommended)
1. Download the latest version of the plugin package [blender-math-animationplug.zip](blender-math-animationplug.zip)
2. Open Preferences in Blender (Edit > Preferences)
3. Click on the "Add-ons" tab
4. Click the "Install..." button
5. Select the downloaded plugin package
6. Enable the plugin (check the checkbox)

### Method 2: Manual packaging and installation
1. Clone or download this repository to your local machine
2. Run the packaging script to generate the zip file:
   ```bash
   python package_addon.py
   ```
3. Follow the steps in Method 1 to install the generated zip file

### Method 3: Development mode installation
1. Clone this repository to your local machine
2. In Blender's add-on settings, click the "Install..." button
3. Select the [__init__.py](file:///G:/GitHubcodecollection/blender-math-animationplug/__init__.py) file in the repository root directory
4. Enable the plugin

## Troubleshooting

### Common Issues and Solutions

1. **Plugin fails to enable with circular import error**
   - Make sure you are using the latest version of the plugin
   - Delete the old version of the plugin in the Blender add-ons directory
   - Reinstall the plugin

2. **UI panel not showing after plugin is enabled**
   - Check if the UI panel on the right side of Blender's 3D view is expanded
   - Check if the "Math Animation" tab is displayed in the UI panel

3. **Missing dependency modules (such as psutil)**
   - The plugin will automatically detect dependencies and prompt you when they are missing
   - Install the required Python packages according to the prompts

4. **LaTeX formula rendering issues**
   - Make sure a LaTeX distribution (such as TeX Live or MiKTeX) is installed on your system
   - Check the LaTeX path configuration in the plugin settings

## Requirements

- Blender 3.0 or higher
- Python 3.7 or higher
- GPU-enabled graphics card recommended for optimal performance

## Documentation

- [User Guide (English)](docs/mcp_user_guide_en.md) | [用户指南 (中文)](docs/mcp_user_guide.md)
- [Developer Documentation (English)](docs/mcp_developer_guide_en.md) | [开发者文档 (中文)](docs/mcp_developer_guide.md)

## Contribution Guidelines

Welcome to submit issue reports and feature suggestions! If you'd like to contribute to the project:

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

```
MIT License

Copyright (c) 2024 [Author Name]

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