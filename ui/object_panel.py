import bpy

class MATH_ANIM_PT_object_panel(bpy.types.Panel):
    bl_label = "创建数学对象"
    bl_idname = "MATH_ANIM_PT_object_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '数学动画'
    bl_parent_id = "MATH_ANIM_PT_main_panel"
    bl_order = 0

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # 添加对象的UI
        layout.operator("math_anim.add_coordinate_system", text="添加坐标系")
        layout.operator("math_anim.add_latex_formula", text="添加LaTeX公式")
        layout.operator("math_anim.add_curve_2d", text="添加2D曲线")
        layout.operator("math_anim.add_surface_3d", text="添加3D曲面")
        layout.operator("math_anim.add_vector_field", text="添加向量场")
        layout.operator("math_anim.add_probability_dist", text="添加概率分布")