import bpy
from .material_system import MaterialSystem
from .lighting import Lighting
from .npr_render import NPRRender
from .special_effects import SpecialEffects
from .style_switcher import StyleSwitcher
from . import operators

def register():
    # 只注册操作符，属性类在properties.py中注册
    operators.register()

def unregister():
    operators.unregister()
