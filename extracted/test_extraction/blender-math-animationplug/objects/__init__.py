import bpy
from .coordinate_system import CoordinateSystem
from .latex_formula import LatexFormula
from .curve_2d import Curve2D
from .surface_3d import Surface3D
from .vector_field import VectorField
from .probability_dist import ProbabilityDistribution
from . import operators

def register():
    bpy.utils.register_class(CoordinateSystem)
    bpy.utils.register_class(LatexFormula)
    bpy.utils.register_class(Curve2D)
    bpy.utils.register_class(Surface3D)
    bpy.utils.register_class(VectorField)
    bpy.utils.register_class(ProbabilityDistribution)
    operators.register()

def unregister():
    operators.unregister()
    bpy.utils.unregister_class(ProbabilityDistribution)
    bpy.utils.unregister_class(VectorField)
    bpy.utils.unregister_class(Surface3D)
    bpy.utils.unregister_class(Curve2D)
    bpy.utils.unregister_class(LatexFormula)
    bpy.utils.unregister_class(CoordinateSystem)