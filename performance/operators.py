import bpy

class ApplyRealtimePreviewOperator(bpy.types.Operator):
    bl_idname = "math_anim.apply_realtime_preview"
    bl_label = "Apply Realtime Preview"

    def execute(self, context):
        props = context.scene.math_anim_properties.performance.realtime_preview
        props.apply()
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

class ApplyGPUAccelerationOperator(bpy.types.Operator):
    bl_idname = "math_anim.apply_gpu_acceleration"
    bl_label = "Apply GPU Acceleration"

    def execute(self, context):
        props = context.scene.math_anim_properties.performance.gpu_acceleration
        props.apply()
        return {'FINISHED'}

class BatchExportOperator(bpy.types.Operator):
    bl_idname = "math_anim.batch_export"
    bl_label = "Batch Export"

    def execute(self, context):
        props = context.scene.math_anim_properties.performance.batch_export
        props.execute_export()
        return {'FINISHED'}


_classes = [
    ApplyRealtimePreviewOperator,
    ApplyMeshSimplificationOperator,
    ApplyGPUAccelerationOperator,
    BatchExportOperator,
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)