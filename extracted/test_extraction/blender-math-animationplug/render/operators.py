import bpy

class ApplyMaterialPresetOperator(bpy.types.Operator):
    bl_idname = "math_anim.apply_material_preset"
    bl_label = "Apply Material Preset"

    def execute(self, context):
        obj = context.active_object
        if obj:
            props = context.scene.math_anim_properties.render.material
            props.apply(obj)
        return {'FINISHED'}

class ApplyLightingPresetOperator(bpy.types.Operator):
    bl_idname = "math_anim.apply_lighting_preset"
    bl_label = "Apply Lighting Preset"

    def execute(self, context):
        props = context.scene.math_anim_properties.render.lighting
        props.apply(context.active_object)
        return {'FINISHED'}

class ApplyNPRSettingsOperator(bpy.types.Operator):
    bl_idname = "math_anim.apply_npr_settings"
    bl_label = "Apply NPR Settings"

    def execute(self, context):
        props = context.scene.math_anim_properties.render.npr
        props.apply()
        return {'FINISHED'}

class ApplySpecialEffectsOperator(bpy.types.Operator):
    bl_idname = "math_anim.apply_special_effects"
    bl_label = "Apply Special Effects"

    def execute(self, context):
        props = context.scene.math_anim_properties.render.effects
        props.apply()
        return {'FINISHED'}

class ApplyStyleOperator(bpy.types.Operator):
    bl_idname = "math_anim.apply_style"
    bl_label = "Apply Style"

    def execute(self, context):
        props = context.scene.math_anim_properties.render.style
        props.apply()
        return {'FINISHED'}


_classes = [
    ApplyMaterialPresetOperator,
    ApplyLightingPresetOperator,
    ApplyNPRSettingsOperator,
    ApplySpecialEffectsOperator,
    ApplyStyleOperator,
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)