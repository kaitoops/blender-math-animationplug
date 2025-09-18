import bpy
from ..core.base import MathObjectBase

class AddCoordinateSystemOperator(bpy.types.Operator):
    bl_idname = "math_anim.add_coordinate_system"
    bl_label = "Add Coordinate System"

    def execute(self, context):
        bpy.ops.object.add(type='EMPTY')
        empty = context.active_object
        empty.name = "CoordinateSystem"
        empty.math_object_properties.type = 'COORDINATE_SYSTEM'
        empty.math_object_properties.update_object(context)
        return {'FINISHED'}

class AddLatexFormulaOperator(bpy.types.Operator):
    bl_idname = "math_anim.add_latex_formula"
    bl_label = "Add LaTeX Formula"

    def execute(self, context):
        bpy.ops.object.add(type='EMPTY')
        empty = context.active_object
        empty.name = "LatexFormula"
        empty.math_object_properties.type = 'LATEX'
        empty.math_object_properties.update_object(context)
        return {'FINISHED'}

class AddCurve2DOperator(bpy.types.Operator):
    bl_idname = "math_anim.add_curve_2d"
    bl_label = "Add 2D Curve"

    def execute(self, context):
        bpy.ops.object.add(type='EMPTY')
        empty = context.active_object
        empty.name = "Curve2D"
        empty.math_object_properties.type = 'CURVE_2D'
        empty.math_object_properties.update_object(context)
        return {'FINISHED'}

class AddSurface3DOperator(bpy.types.Operator):
    bl_idname = "math_anim.add_surface_3d"
    bl_label = "Add 3D Surface"

    def execute(self, context):
        bpy.ops.object.add(type='EMPTY')
        empty = context.active_object
        empty.name = "Surface3D"
        empty.math_object_properties.type = 'SURFACE_3D'
        empty.math_object_properties.update_object(context)
        return {'FINISHED'}

class AddVectorFieldOperator(bpy.types.Operator):
    bl_idname = "math_anim.add_vector_field"
    bl_label = "Add Vector Field"

    def execute(self, context):
        bpy.ops.object.add(type='EMPTY')
        empty = context.active_object
        empty.name = "VectorField"
        empty.math_object_properties.type = 'VECTOR_FIELD'
        empty.math_object_properties.update_object(context)
        return {'FINISHED'}

class AddProbabilityDistributionOperator(bpy.types.Operator):
    bl_idname = "math_anim.add_probability_dist"
    bl_label = "Add Probability Distribution"

    def execute(self, context):
        bpy.ops.object.add(type='EMPTY')
        empty = context.active_object
        empty.name = "ProbabilityDistribution"
        empty.math_object_properties.type = 'PROBABILITY_DISTRIBUTION'
        empty.math_object_properties.update_object(context)
        return {'FINISHED'}


_classes = [
    AddCoordinateSystemOperator,
    AddLatexFormulaOperator,
    AddCurve2DOperator,
    AddSurface3DOperator,
    AddVectorFieldOperator,
    AddProbabilityDistributionOperator,
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)