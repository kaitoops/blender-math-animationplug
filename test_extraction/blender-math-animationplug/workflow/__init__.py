import bpy
from .templates import TemplateManager
from .formula_editor import FormulaEditor
from .error_diagnostic import ErrorDiagnostic
from .interactive_tutorial import InteractiveTutorial
from . import operators

def register():
    bpy.utils.register_class(TemplateManager)
    bpy.utils.register_class(FormulaEditor)
    bpy.utils.register_class(ErrorDiagnostic)
    bpy.utils.register_class(InteractiveTutorial)
    operators.register()

def unregister():
    operators.unregister()
    bpy.utils.unregister_class(InteractiveTutorial)
    bpy.utils.unregister_class(ErrorDiagnostic)
    bpy.utils.unregister_class(FormulaEditor)
    bpy.utils.unregister_class(TemplateManager)