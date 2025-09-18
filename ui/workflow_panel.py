import bpy

class MATH_ANIM_PT_workflow_panel(bpy.types.Panel):
    bl_label = "工作流优化"
    bl_idname = "MATH_ANIM_PT_workflow_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '数学动画'
    bl_parent_id = "MATH_ANIM_PT_main_panel"
    bl_order = 4

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        wf_props = scene.math_anim_properties.workflow

        # 一键模板
        box = layout.box()
        box.label(text="一键模板")
        box.prop(wf_props.templates, "template")
        box.operator("math_anim.apply_template")

        # 公式编辑器
        box = layout.box()
        box.label(text="LaTeX公式编辑器")
        wf_props.formula_editor.draw(box)
        # 使用不同的方式处理操作符，避免直接访问属性
        if context.active_object:
            op = box.operator("math_anim.show_formula_editor", text="应用到选中对象")
            op.target_object_name = context.active_object.name
        else:
            box.operator("math_anim.show_formula_editor", text="显示公式编辑器")

        # 交互式教程
        box = layout.box()
        box.label(text="帮助")
        box.operator("math_anim.start_interactive_tutorial", text="开始交互式教程")