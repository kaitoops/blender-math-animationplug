# MCP Animation Control Module User Guide

[English Version](mcp_user_guide_en.md) | [中文版本](mcp_user_guide.md)

## Introduction

The MCP (Motion Capture) animation control module is an important component of the Blender math animation plugin. It provides powerful motion capture data processing and application functions. This module supports animation data loading, bone mapping, animation application, and performance optimization.

## Features

- Support for importing motion capture data in multiple formats
- Flexible bone mapping system with template saving and reuse
- Intelligent animation data processing and optimization
- Adjustable performance optimization levels
- Complete error handling and logging

## Usage

### 1. Interface Layout

The MCP control panel is located in the sidebar of the 3D view (press N to open), containing the following main areas:

- File Settings: Select MCP data file
- Animation Control: Set start and end frames of the animation
- Animation Settings: Adjust smoothing coefficient and auto-scaling options
- Bone Mapping: Manage bone mapping templates
- Performance Settings: Adjust performance optimization level
- Action Buttons: Load, apply, and clean up animation

### 2. Basic Workflow

1. **Preparation**
   - Import or create target bone rig
   - Prepare MCP motion capture data file

2. **Load Animation**
   - Select MCP data file in file settings
   - Click the "Load Animation" button

3. **Set Mapping**
   - Select an existing mapping template, or
   - Create a new bone mapping and save as template

4. **Apply Animation**
   - Select target bone rig
   - Set animation parameters (start frame, end frame, etc.)
   - Click the "Apply Animation" button

5. **Optimization and Adjustment**
   - Adjust smoothing coefficient to achieve desired animation effect
   - Enable auto-scaling as needed
   - Adjust performance level to balance quality and performance

### 3. Performance Optimization

Performance level settings provide three options:

- **Low**: Prioritize performance, suitable for preview or real-time feedback
- **Medium**: Balance performance and quality, suitable for most situations
- **High**: Prioritize quality, suitable for final rendering

### 4. Bone Mapping Templates

Bone mapping templates can save commonly used mapping configurations for reuse in different projects:

1. **Create Template**
   - Complete bone mapping setup
   - Click the "Save Mapping Template" button
   - Enter template name and save

2. **Use Template**
   - Select a saved template from the dropdown list
   - Template will be automatically applied to the current bone rig

## Best Practices

1. **Data Preparation**
   - Ensure MCP data format is correct
   - Pre-clean and standardize motion data

2. **Performance Optimization**
   - Use low or medium performance levels during production
   - Use high performance level for final rendering
   - Adjust smoothing coefficient appropriately to avoid over-smoothing

3. **Bone Mapping**
   - Create mapping templates for commonly used bone structures
   - Regularly check and update mapping relationships
   - Use meaningful template names

4. **Workflow Optimization**
   - Test settings on short animation segments first
   - Keep scene files clean
   - Save work regularly

## Troubleshooting

1. **Loading Failure**
   - Check if file format is supported
   - Confirm file path is correct
   - Check error log for detailed information

2. **Application Failure**
   - Ensure correct bone rig is selected
   - Check if bone mapping is complete
   - Verify animation frame range settings

3. **Performance Issues**
   - Try lowering performance level
   - Reduce other objects in the scene
   - Turn off unnecessary viewport effects

## Technical Support

If you encounter problems or need help:

1. Check error log for detailed information
2. Check if you are using the latest version
3. Report issues through the project's Issue system

## Version History

### v1.0.0
- Initial version release
- Support for basic MCP data processing
- Implementation of bone mapping system
- Added performance optimization features