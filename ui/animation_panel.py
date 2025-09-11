import bpy

class MATH_ANIM_PT_animation_panel(bpy.types.Panel):
    bl_label = "动画系统"
    bl_idname = "MATH_ANIM_PT_animation_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '数学动画'
    bl_parent_id = "MATH_ANIM_PT_main_panel"
    bl_order = 1

    def draw(self, context):
        layout = self.layout
        obj = context.active_object

        if not obj:
            layout.label(text="请选择一个对象")
            return

        # 获取或创建动画属性
        anim_props = obj.math_anim_properties.animation

        # 变换动画
        box = layout.box()
        box.label(text="变换动画")
        box.prop(anim_props.transform, "use_transform")
        if anim_props.transform.use_transform:
            box.prop(anim_props.transform, "start_frame")
            box.prop(anim_props.transform, "end_frame")
            box.prop(anim_props.transform, "start_location")
            box.prop(anim_props.transform, "end_location")
            box.operator("math_anim.apply_transform_animation")

        # 路径绘制
        box = layout.box()
        box.label(text="路径绘制")
        box.prop(anim_props.path_drawing, "use_path_drawing")
        if anim_props.path_drawing.use_path_drawing:
            box.prop(anim_props.path_drawing, "target_curve")
            box.prop(anim_props.path_drawing, "start_frame")
            box.prop(anim_props.path_drawing, "end_frame")
            box.operator("math_anim.apply_path_drawing_animation")