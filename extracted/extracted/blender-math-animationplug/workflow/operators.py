import bpy

class ApplyTemplateOperator(bpy.types.Operator):
    bl_idname = "math_anim.apply_template"
    bl_label = "Apply Template"

    def execute(self, context):
        props = context.scene.math_anim_properties.workflow.templates
        props.apply_template()
        return {'FINISHED'}

class ShowFormulaEditorOperator(bpy.types.Operator):
    bl_idname = "math_anim.show_formula_editor"
    bl_label = "Show Formula Editor"

    def execute(self, context):
        props = context.scene.math_anim_properties.workflow.formula_editor
        # Logic to show the formula editor UI
        return {'FINISHED'}

class StartInteractiveTutorialOperator(bpy.types.Operator):
    bl_idname = "math_anim.start_interactive_tutorial"
    bl_label = "Start Interactive Tutorial"

    def execute(self, context):
        props = context.scene.math_anim_properties.workflow.interactive_tutorial
        props.start()
        return {'FINISHED'}


_classes = [
    ApplyTemplateOperator,
    ShowFormulaEditorOperator,
    StartInteractiveTutorialOperator,
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)