import bpy

class MATH_ANIM_PT_render_panel(bpy.types.Panel):
    bl_label = "渲染与风格化"
    bl_idname = "MATH_ANIM_PT_render_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '数学动画'
    bl_parent_id = "MATH_ANIM_PT_main_panel"
    bl_order = 2

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        render_props = scene.math_anim_properties.render

        # 材质系统
        box = layout.box()
        box.label(text="材质系统")
        box.prop(render_props.material, "preset")
        box.operator("math_anim.apply_material_preset")

        # 灯光系统
        box = layout.box()
        box.label(text="灯光系统")
        box.prop(render_props.lighting, "preset")
        box.prop(render_props.lighting, "intensity")
        box.operator("math_anim.apply_lighting_preset")

        # NPR
        box = layout.box()
        box.label(text="NPR渲染")
        box.prop(render_props.npr, "use_outline")
        if render_props.npr.use_outline:
            box.prop(render_props.npr, "outline_color")
        box.operator("math_anim.apply_npr_settings")

        # 特效
        box = layout.box()
        box.label(text="后期特效")
        box.prop(render_props.effects, "use_bloom")
        if render_props.effects.use_bloom:
            box.prop(render_props.effects, "bloom_intensity")
        box.prop(render_props.effects, "use_motion_blur")
        box.operator("math_anim.apply_special_effects")

        # 风格切换
        box = layout.box()
        box.label(text="一键风格")
        box.prop(render_props.style, "style")
        box.operator("math_anim.apply_style")