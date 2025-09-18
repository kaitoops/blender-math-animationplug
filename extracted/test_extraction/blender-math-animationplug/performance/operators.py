import bpy

class EnableDisableRealtimePreviewOperator(bpy.types.Operator):
    bl_idname = "math_anim.enable_disable_realtime_preview"
    bl_label = "Enable/Disable Realtime Preview"

    def execute(self, context):
        props = context.scene.math_anim_properties.performance.realtime_preview
        props.enabled = not props.enabled
        return {'FINISHED'}

class ApplyMeshSimplificationOperator(bpy.types.Operator):
    bl_idname = "math_anim.apply_mesh_simplification"
    bl_label = "Apply Mesh Simplification"

    def execute(self, context):
        obj = context.active_object
        if obj:
            props = context.scene.math_anim_properties.performance.mesh_simplification
            props.apply(obj)
        return {'FINISHED'}

class EnableDisableGPUAccelerationOperator(bpy.types.Operator):
    bl_idname = "math_anim.enable_disable_gpu_acceleration"
    bl_label = "Enable/Disable GPU Acceleration"

    def execute(self, context):
        props = context.scene.math_anim_properties.performance.gpu_acceleration
        props.enabled = not props.enabled
        return {'FINISHED'}

class BatchExportOperator(bpy.types.Operator):
    bl_idname = "math_anim.batch_export"
    bl_label = "Batch Export"

    def execute(self, context):
        props = context.scene.math_anim_properties.performance.batch_export
        props.execute_export()
        return {'FINISHED'}


_classes = [
    EnableDisableRealtimePreviewOperator,
    ApplyMeshSimplificationOperator,
    EnableDisableGPUAccelerationOperator,
    BatchExportOperator,
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)