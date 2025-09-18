import bpy
from bpy.props import PointerProperty, StringProperty, FloatProperty

class MorphAnimation(bpy.types.PropertyGroup):
    """形态变形动画类，使用形状关键帧"""
    
    target_mesh = PointerProperty(
        name="Target Mesh",
        description="Mesh object to animate",
        type=bpy.types.Object
    )
    
    start_frame = FloatProperty(
        name="Start Frame",
        description="Animation start frame",
        default=1.0
    )
    
    end_frame = FloatProperty(
        name="End Frame",
        description="Animation end frame",
        default=100.0
    )
    
    shape_key_name = StringProperty(
        name="Shape Key Name",
        description="Name of the shape key to animate"
    )
    
    start_value = FloatProperty(
        name="Start Value",
        description="Shape key value at start frame",
        default=0.0,
        min=0.0,
        max=1.0
    )
    
    end_value = FloatProperty(
        name="End Value",
        description="Shape key value at end frame",
        default=1.0,
        min=0.0,
        max=1.0
    )
    
    def apply(self):
        """应用形态变形动画"""
        if not self.target_mesh or self.target_mesh.type != 'MESH':
            return
        
        shape_keys = self.target_mesh.data.shape_keys
        if not shape_keys or self.shape_key_name not in shape_keys.key_blocks:
            return
        
        key_block = shape_keys.key_blocks[self.shape_key_name]
        
        # 插入关键帧
        key_block.value = self.start_value
        key_block.keyframe_insert(data_path="value", frame=self.start_frame)
        key_block.value = self.end_value
        key_block.keyframe_insert(data_path="value", frame=self.end_frame)
    
    def remove(self):
        """移除形态变形动画"""
        if not self.target_mesh or self.target_mesh.type != 'MESH':
            return
        
        shape_keys = self.target_mesh.data.shape_keys
        if not shape_keys or self.shape_key_name not in shape_keys.key_blocks:
            return
        
        key_block = shape_keys.key_blocks[self.shape_key_name]
        
        # 移除动画数据
        if shape_keys.animation_data and shape_keys.animation_data.action:
            fcurves_to_remove = []
            for fcurve in shape_keys.animation_data.action.fcurves:
                if fcurve.data_path == f'key_blocks["{self.shape_key_name}"].value':
                    fcurves_to_remove.append(fcurve)
            
            for fcurve in fcurves_to_remove:
                shape_keys.animation_data.action.fcurves.remove(fcurve)
        
        # 重置值
        key_block.value = 0.0