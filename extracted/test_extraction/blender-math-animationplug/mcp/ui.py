import bpy
from bpy.props import StringProperty, IntProperty, FloatProperty, BoolProperty
from ..core.error_handling import error_handler, PerformanceLevel

class MATH_ANIM_PT_mcp_panel(bpy.types.Panel):
    bl_label = "MCP动画控制"
    bl_idname = "MATH_ANIM_PT_mcp_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "数学动画"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mcp = scene.mcp_animation_controller
        
        # 文件选择区域
        box = layout.box()
        box.label(text="文件设置")
        box.prop(mcp, "mcp_file")
        
        # 动画控制区域
        box = layout.box()
        box.label(text="动画控制")
        row = box.row()
        row.prop(mcp, "start_frame")
        row.prop(mcp, "end_frame")
        
        # 动画设置区域
        box = layout.box()
        box.label(text="动画设置")
        box.prop(mcp, "smoothing_factor")
        box.prop(mcp, "auto_scale")
        
        # 骨骼映射设置区域
        box = layout.box()
        box.label(text="骨骼映射")
        box.prop(mcp, "mapping_template")
        row = box.row()
        row.operator("math_anim.save_mcp_mapping", text="保存映射模板")
        
        # 性能设置区域
        box = layout.box()
        box.label(text="性能设置")
        row = box.row()
        row.operator("math_anim.set_mcp_performance", text="设置性能级别")
        
        # 操作按钮区域
        box = layout.box()
        box.label(text="操作")
        row = box.row()
        row.operator("math_anim.load_mcp_animation", text="加载动画")
        row.operator("math_anim.apply_mcp_animation", text="应用动画")
        row = box.row()
        row.operator("math_anim.cleanup_mcp_animation", text="清理")

class LoadMCPAnimationOperator(bpy.types.Operator):
    """加载MCP动画数据"""
    bl_idname = "math_anim.load_mcp_animation"
    bl_label = "加载MCP动画"
    
    def execute(self, context):
        try:
            mcp = context.scene.math_anim_properties.mcp
            if mcp.load_animation(context):
                self.report({'INFO'}, "成功加载MCP动画数据")
                return {'FINISHED'}
            else:
                self.report({'ERROR'}, "加载MCP动画数据失败")
                return {'CANCELLED'}
        except Exception as e:
            error_handler.handle_object_error(e, "Loading MCP animation")
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}

class ApplyMCPAnimationOperator(bpy.types.Operator):
    """应用MCP动画到骨骼装备"""
    bl_idname = "math_anim.apply_mcp_animation"
    bl_label = "应用MCP动画"
    
    def execute(self, context):
        try:
            mcp = context.scene.math_anim_properties.mcp
            armature = context.active_object
            
            if not armature or armature.type != 'ARMATURE':
                self.report({'ERROR'}, "请选择一个骨骼装备")
                return {'CANCELLED'}
            
            if mcp.apply_animation(context, armature):
                self.report({'INFO'}, "成功应用MCP动画")
                return {'FINISHED'}
            else:
                self.report({'ERROR'}, "应用MCP动画失败")
                return {'CANCELLED'}
        except Exception as e:
            error_handler.handle_object_error(e, "Applying MCP animation")
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}

class CleanupMCPAnimationOperator(bpy.types.Operator):
    """清理MCP动画数据"""
    bl_idname = "math_anim.cleanup_mcp_animation"
    bl_label = "清理MCP动画"
    
    def execute(self, context):
        try:
            mcp = context.scene.math_anim_properties.mcp
            mcp.cleanup()
            self.report({'INFO'}, "成功清理MCP动画数据")
            return {'FINISHED'}
        except Exception as e:
            error_handler.handle_object_error(e, "Cleaning up MCP animation")
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}

class SaveMCPMappingOperator(bpy.types.Operator):
    """保存MCP骨骼映射模板"""
    bl_idname = "math_anim.save_mcp_mapping"
    bl_label = "保存映射模板"
    
    template_name: StringProperty(
        name="模板名称",
        description="输入映射模板名称",
        default=""
    )
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "template_name")
    
    def execute(self, context):
        try:
            if not self.template_name:
                self.report({'ERROR'}, "请输入模板名称")
                return {'CANCELLED'}
            
            mcp = context.scene.math_anim_properties.mcp
            if mcp.save_mapping_template(self.template_name):
                self.report({'INFO'}, f"成功保存映射模板: {self.template_name}")
                return {'FINISHED'}
            else:
                self.report({'ERROR'}, "保存映射模板失败")
                return {'CANCELLED'}
        except Exception as e:
            error_handler.handle_object_error(e, "Saving mapping template")
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}

class SetMCPPerformanceOperator(bpy.types.Operator):
    bl_idname = "math_anim.set_mcp_performance"
    bl_label = "设置MCP性能级别"
    bl_description = "设置MCP动画的性能优化级别"
    
    performance_level: bpy.props.EnumProperty(
        name="性能级别",
        description="选择性能优化级别",
        items=[
            ("LOW", "低", "优先考虑性能，可能影响动画质量"),
            ("NORMAL", "中", "平衡性能和质量"),
            ("HIGH", "高", "优先考虑质量，可能影响性能")
        ],
        default="NORMAL"
    )
    
    def execute(self, context):
        try:
            mcp = context.scene.mcp_animation_controller
            level_mapping = {
                "LOW": PerformanceLevel.LOW,
                "NORMAL": PerformanceLevel.NORMAL,
                "HIGH": PerformanceLevel.HIGH
            }
            level = level_mapping.get(self.performance_level, PerformanceLevel.NORMAL)
            mcp.set_performance_level(level)
            self.report({"INFO"}, f"已设置性能级别为: {self.performance_level}")
            return {"FINISHED"}
        except Exception as e:
            error_handler.handle_object_error(e, "Setting MCP performance level")
            return {"CANCELLED"}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "performance_level")

_classes = [
    MATH_ANIM_PT_mcp_panel,
    LoadMCPAnimationOperator,
    ApplyMCPAnimationOperator,
    CleanupMCPAnimationOperator,
    SaveMCPMappingOperator,
    SetMCPPerformanceOperator
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)