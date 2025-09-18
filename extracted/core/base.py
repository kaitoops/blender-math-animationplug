import bpy
from bpy.props import FloatVectorProperty, StringProperty, BoolProperty
from .error_handling import error_handler, ObjectError, PerformanceLevel
import time
import abc

class MathObjectBase(bpy.types.PropertyGroup):
    """基类：所有数学对象的基础类"""
    
    # 通用属性
    location = FloatVectorProperty(
        name="Location",
        description="Object location in 3D space",
        subtype='TRANSLATION',
        default=(0.0, 0.0, 0.0)
    )
    
    visibility = BoolProperty(
        name="Visibility",
        description="Toggle object visibility",
        default=True
    )
    
    label = StringProperty(
        name="Label",
        description="Object label/name",
        default=""
    )

    def __init__(self):
        super().__init__()
        self.obj = None
        self._creation_time = None
    
    def create(self):
        """创建数学对象的几何体"""
        try:
            start_time = time.time()
            self._create_implementation()
            end_time = time.time()
            self._creation_time = end_time - start_time
            
            error_handler.log_performance(
                PerformanceLevel.INFO,
                f"Created {self.__class__.__name__} in {self._creation_time:.3f} seconds"
            )
        except Exception as e:
            error_handler.handle_object_error(e, f"Creating {self.__class__.__name__}")
    
    def _create_implementation(self):
        """实际的创建实现 - 子类需要重写此方法"""
        raise NotImplementedError("Subclasses must implement _create_implementation method")
    
    def update(self):
        """更新对象属性和几何体"""
        try:
            if not self.obj:
                raise ObjectError(f"Cannot update {self.__class__.__name__}: Object reference is None")
            
            start_time = time.time()
            self._update_implementation()
            end_time = time.time()
            
            update_time = end_time - start_time
            error_handler.log_performance(
                PerformanceLevel.INFO,
                f"Updated {self.__class__.__name__} in {update_time:.3f} seconds"
            )
        except Exception as e:
            error_handler.handle_object_error(e, f"Updating {self.__class__.__name__}")
    
    def _update_implementation(self):
        """实际的更新实现 - 子类需要重写此方法"""
        raise NotImplementedError("Subclasses must implement _update_implementation method")
    
    def delete(self):
        """删除对象"""
        try:
            if self.obj:
                self._delete_implementation()
                self.obj = None
        except Exception as e:
            error_handler.handle_object_error(e, f"Deleting {self.__class__.__name__}")
    
    def _delete_implementation(self):
        """实际的删除实现 - 子类需要重写此方法"""
        raise NotImplementedError("Subclasses must implement _delete_implementation method")
    
    def add_to_scene(self):
        """将对象添加到场景中"""
        try:
            if not self.obj:
                self.create()
            
            if self.obj and self.obj.name not in bpy.context.scene.objects:
                bpy.context.scene.collection.objects.link(self.obj)
                error_handler.log_performance(
                    PerformanceLevel.INFO,
                    f"Added {self.__class__.__name__} to scene"
                )
        except Exception as e:
            error_handler.handle_scene_error(e, f"Adding {self.__class__.__name__} to scene")
    
    def remove_from_scene(self):
        """从场景中移除对象"""
        try:
            if self.obj and self.obj.name in bpy.context.scene.objects:
                bpy.context.scene.collection.objects.unlink(self.obj)
                error_handler.log_performance(
                    PerformanceLevel.INFO,
                    f"Removed {self.__class__.__name__} from scene"
                )
        except Exception as e:
            error_handler.handle_scene_error(e, f"Removing {self.__class__.__name__} from scene")
            
    def __del__(self):
        """析构函数：确保对象被正确清理"""
        try:
            self.delete()
        except Exception as e:
            error_handler.log_performance(
                PerformanceLevel.WARNING,
                f"Error during cleanup of {self.__class__.__name__}: {str(e)}"
            )