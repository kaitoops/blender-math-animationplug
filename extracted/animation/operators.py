import bpy

class ApplyTransformAnimationOperator(bpy.types.Operator):
    bl_idname = "math_anim.apply_transform_animation"
    bl_label = "Apply Transform Animation"

    def execute(self, context):
        obj = context.active_object
        if obj:
            props = obj.math_anim_properties.animation.transform
            props.apply(obj)
        return {'FINISHED'}

class ApplyPathDrawingAnimationOperator(bpy.types.Operator):
    bl_idname = "math_anim.apply_path_drawing_animation"
    bl_label = "Apply Path Drawing Animation"

    def execute(self, context):
        obj = context.active_object
        if obj:
            props = obj.math_anim_properties.animation.path_drawing
            props.apply(obj)
        return {'FINISHED'}


_classes = [
    ApplyTransformAnimationOperator,
    ApplyPathDrawingAnimationOperator,
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)