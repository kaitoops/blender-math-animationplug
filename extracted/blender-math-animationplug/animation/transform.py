import bpy
from bpy.props import PointerProperty, FloatVectorProperty, FloatProperty, EnumProperty

class TransformAnimation(bpy.types.PropertyGroup):
    """变换动画类，控制对象的位置、旋转和缩放"""
    
    target_object = PointerProperty(
        name="Target Object",
        description="Object to animate",
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
    
    start_location = FloatVectorProperty(
        name="Start Location",
        description="Start location of the object",
        subtype='TRANSLATION'
    )
    
    end_location = FloatVectorProperty(
        name="End Location",
        description="End location of the object",
        subtype='TRANSLATION'
    )
    
    start_rotation = FloatVectorProperty(
        name="Start Rotation",
        description="Start rotation of the object (Euler angles)",
        subtype='EULER'
    )
    
    end_rotation = FloatVectorProperty(
        name="End Rotation",
        description="End rotation of the object (Euler angles)",
        subtype='EULER'
    )
    
    start_scale = FloatVectorProperty(
        name="Start Scale",
        description="Start scale of the object",
        subtype='XYZ'
    )
    
    end_scale = FloatVectorProperty(
        name="End Scale",
        description="End scale of the object",
        subtype='XYZ'
    )
    
    interpolation = EnumProperty(
        name="Interpolation",
        description="Keyframe interpolation type",
        items=[
            ('LINEAR', 'Linear', 'Linear interpolation'),
            ('BEZIER', 'Bezier', 'Bezier interpolation'),
            ('SINE', 'Sine', 'Sinusoidal interpolation'),
            ('QUAD', 'Quadratic', 'Quadratic interpolation'),
            ('CUBIC', 'Cubic', 'Cubic interpolation'),
            ('QUART', 'Quartic', 'Quartic interpolation'),
            ('QUINT', 'Quintic', 'Quintic interpolation'),
            ('EXPO', 'Exponential', 'Exponential interpolation'),
            ('CIRC', 'Circular', 'Circular interpolation'),
            ('BACK', 'Back', 'Back-in/out interpolation'),
            ('BOUNCE', 'Bounce', 'Bouncing interpolation'),
            ('ELASTIC', 'Elastic', 'Elastic interpolation')
        ],
        default='BEZIER'
    )
    
    def apply(self):
        """应用变换动画"""
        if not self.target_object:
            return
        
        # 插入位置关键帧
        self.target_object.location = self.start_location
        self.target_object.keyframe_insert(data_path="location", frame=self.start_frame)
        self.target_object.location = self.end_location
        self.target_object.keyframe_insert(data_path="location", frame=self.end_frame)
        
        # 插入旋转关键帧
        self.target_object.rotation_euler = self.start_rotation
        self.target_object.keyframe_insert(data_path="rotation_euler", frame=self.start_frame)
        self.target_object.rotation_euler = self.end_rotation
        self.target_object.keyframe_insert(data_path="rotation_euler", frame=self.end_frame)
        
        # 插入缩放关键帧
        self.target_object.scale = self.start_scale
        self.target_object.keyframe_insert(data_path="scale", frame=self.start_frame)
        self.target_object.scale = self.end_scale
        self.target_object.keyframe_insert(data_path="scale", frame=self.end_frame)
        
        # 设置插值模式
        if self.target_object.animation_data and self.target_object.animation_data.action:
            for fcurve in self.target_object.animation_data.action.fcurves:
                for keyframe in fcurve.keyframe_points:
                    if keyframe.co.x >= self.start_frame and keyframe.co.x <= self.end_frame:
                        keyframe.interpolation = self.interpolation
    
    def remove(self):
        """移除变换动画"""
        if not self.target_object or not self.target_object.animation_data or not self.target_object.animation_data.action:
            return
        
        action = self.target_object.animation_data.action
        
        # 移除关键帧
        for fcurve in action.fcurves:
            keyframes_to_remove = []
            for keyframe in fcurve.keyframe_points:
                if keyframe.co.x >= self.start_frame and keyframe.co.x <= self.end_frame:
                    keyframes_to_remove.append(keyframe)
            
            for keyframe in keyframes_to_remove:
                fcurve.keyframe_points.remove(keyframe)