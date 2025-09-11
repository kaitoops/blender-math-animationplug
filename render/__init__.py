import bpy
from .material_system import MaterialSystem
from .lighting import Lighting
from .npr_render import NPRRender
from .special_effects import SpecialEffects
from .style_switcher import StyleSwitcher
from . import operators

def register():
    bpy.utils.register_class(MaterialSystem)
    bpy.utils.register_class(Lighting)
    bpy.utils.register_class(NPRRender)
    bpy.utils.register_class(SpecialEffects)
    bpy.utils.register_class(StyleSwitcher)
    operators.register()

def unregister():
    operators.unregister()
    bpy.utils.unregister_class(StyleSwitcher)
    bpy.utils.unregister_class(SpecialEffects)
    bpy.utils.unregister_class(NPRRender)
    bpy.utils.unregister_class(Lighting)
    bpy.utils.unregister_class(MaterialSystem)