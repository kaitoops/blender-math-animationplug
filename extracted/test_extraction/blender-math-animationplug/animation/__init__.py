import bpy
from .transform import TransformAnimation
from .path_drawing import PathDrawing
from .morphing import MorphAnimation
from .fluid import FluidAnimation
from .formula_evolution import FormulaEvolution
from . import operators

def register():
    bpy.utils.register_class(TransformAnimation)
    bpy.utils.register_class(PathDrawing)
    bpy.utils.register_class(MorphAnimation)
    bpy.utils.register_class(FluidAnimation)
    bpy.utils.register_class(FormulaEvolution)
    operators.register()

def unregister():
    operators.unregister()
    bpy.utils.unregister_class(FormulaEvolution)
    bpy.utils.unregister_class(FluidAnimation)
    bpy.utils.unregister_class(MorphAnimation)
    bpy.utils.unregister_class(PathDrawing)
    bpy.utils.unregister_class(TransformAnimation)