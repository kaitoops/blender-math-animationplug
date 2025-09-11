import bpy
from .realtime_preview import RealtimePreview
from .mesh_simplification import MeshSimplification
from .gpu_acceleration import GPUAcceleration
from .batch_export import BatchExport
from . import operators

def register():
    bpy.utils.register_class(RealtimePreview)
    bpy.utils.register_class(MeshSimplification)
    bpy.utils.register_class(GPUAcceleration)
    bpy.utils.register_class(BatchExport)
    operators.register()

def unregister():
    operators.unregister()
    bpy.utils.unregister_class(BatchExport)
    bpy.utils.unregister_class(GPUAcceleration)
    bpy.utils.unregister_class(MeshSimplification)
    bpy.utils.unregister_class(RealtimePreview)