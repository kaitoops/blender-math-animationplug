import bpy
from .base import MathObjectBase
from .scene_manager import SceneManager
from .dependency_checker import DependencyChecker

def register():
    bpy.utils.register_class(MathObjectBase)
    SceneManager.register()
    DependencyChecker.check_dependencies()

def unregister():
    bpy.utils.unregister_class(MathObjectBase)
    SceneManager.unregister()