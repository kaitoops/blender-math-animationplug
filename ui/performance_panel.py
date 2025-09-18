import bpy

class MATH_ANIM_PT_performance_panel(bpy.types.Panel):
    bl_label = "性能优化"
    bl_idname = "MATH_ANIM_PT_performance_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '数学动画'
    bl_parent_id = "MATH_ANIM_PT_main_panel"
    bl_order = 3

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        perf_props = scene.math_anim_properties.performance

        # 实时预览
        box = layout.box()
        box.label(text="实时预览")
        box.prop(perf_props.realtime_preview, "use_simplify")
        box.prop(perf_props.realtime_preview, "display_mode")
        box.operator("math_anim.apply_realtime_preview")

        # 网格简化
        box = layout.box()
        box.label(text="网格简化")
        box.prop(perf_props.mesh_simplification, "ratio")
        box.prop(perf_props.mesh_simplification, "method")
        box.operator("math_anim.apply_mesh_simplification")

        # GPU加速
        box = layout.box()
        box.label(text="GPU加速")
        box.prop(perf_props.gpu_acceleration, "use_gpu")
        box.operator("math_anim.apply_gpu_acceleration")

        # 批量导出
        box = layout.box()
        box.label(text="批量导出")
        box.prop(perf_props.batch_export, "output_path")
        box.prop(perf_props.batch_export, "file_format")
        box.prop(perf_props.batch_export, "start_frame")
        box.prop(perf_props.batch_export, "end_frame")
        box.operator("math_anim.batch_export")