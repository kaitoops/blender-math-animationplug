import bpy
from .templates import TemplateManager
from .formula_editor import FormulaEditor
from .error_diagnostic import ErrorDiagnostic
from .interactive_tutorial import InteractiveTutorial
from . import operators

def register():
    # 只注册操作符，属性类在properties.py中注册
    operators.register()

def unregister():
    operators.unregister()