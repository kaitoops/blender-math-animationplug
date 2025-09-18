import bpy
from bpy.props import CollectionProperty, PointerProperty
from .base import MathObjectBase

class SceneManager:
    """管理数学对象的场景图结构和层级关系"""
    
    @classmethod
    def register(cls):
        # 注册场景属性
        bpy.types.Scene.math_objects = CollectionProperty(
            type=MathObjectBase,
            name="Math Objects",
            description="Collection of mathematical objects in the scene"
        )
        
        bpy.types.Scene.active_math_object = PointerProperty(
            type=MathObjectBase,
            name="Active Math Object",
            description="Currently selected mathematical object"
        )
    
    @classmethod
    def unregister(cls):
        # 注销场景属性
        del bpy.types.Scene.math_objects
        del bpy.types.Scene.active_math_object
    
    @staticmethod
    def add_object(obj):
        """添加数学对象到场景"""
        if isinstance(obj, MathObjectBase):
            scene = bpy.context.scene
            obj.add_to_scene()
            scene.math_objects.add().obj = obj
    
    @staticmethod
    def remove_object(obj):
        """从场景中移除数学对象"""
        if isinstance(obj, MathObjectBase):
            scene = bpy.context.scene
            obj.remove_from_scene()
            for i, math_obj in enumerate(scene.math_objects):
                if math_obj.obj == obj:
                    scene.math_objects.remove(i)
                    break
    
    @staticmethod
    def set_parent(child, parent):
        """设置对象的父子关系"""
        if isinstance(child, MathObjectBase) and isinstance(parent, MathObjectBase):
            if child.obj and parent.obj:
                child.obj.parent = parent.obj
    
    @staticmethod
    def clear_parent(child):
        """清除对象的父子关系"""
        if isinstance(child, MathObjectBase) and child.obj:
            child.obj.parent = None
    
    @staticmethod
    def get_children(parent):
        """获取对象的所有子对象"""
        children = []
        if isinstance(parent, MathObjectBase) and parent.obj:
            for obj in bpy.context.scene.math_objects:
                if obj.obj and obj.obj.parent == parent.obj:
                    children.append(obj)
        return children
    
    @staticmethod
    def update_hierarchy():
        """更新场景中所有数学对象的层级关系"""
        for obj in bpy.context.scene.math_objects:
            if obj.obj:
                obj.update()