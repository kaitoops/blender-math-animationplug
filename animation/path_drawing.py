import bpy
from bpy.props import PointerProperty, FloatProperty, BoolProperty

class PathDrawing(bpy.types.PropertyGroup):
    """路径绘制动画类，模拟笔画生长效果"""
    
    target_curve = PointerProperty(
        name="Target Curve",
        description="Curve object to animate",
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
    
    reverse = BoolProperty(
        name="Reverse",
        description="Reverse the drawing direction",
        default=False
    )
    
    def apply(self):
        """应用路径绘制动画"""
        if not self.target_curve or self.target_curve.type != 'CURVE':
            return
        
        curve_data = self.target_curve.data
        
        # 设置曲线的斜角起始和结束
        curve_data.bevel_factor_start = 0.0 if not self.reverse else 1.0
        curve_data.bevel_factor_end = 1.0 if not self.reverse else 0.0
        
        # 插入起始关键帧
        if not self.reverse:
            curve_data.keyframe_insert(data_path="bevel_factor_end", frame=self.start_frame)
            curve_data.bevel_factor_end = 0.0
            curve_data.keyframe_insert(data_path="bevel_factor_end", frame=self.start_frame)
            curve_data.bevel_factor_end = 1.0
            curve_data.keyframe_insert(data_path="bevel_factor_end", frame=self.end_frame)
        else:
            curve_data.keyframe_insert(data_path="bevel_factor_start", frame=self.start_frame)
            curve_data.bevel_factor_start = 1.0
            curve_data.keyframe_insert(data_path="bevel_factor_start", frame=self.start_frame)
            curve_data.bevel_factor_start = 0.0
            curve_data.keyframe_insert(data_path="bevel_factor_start", frame=self.end_frame)
    
    def remove(self):
        """移除路径绘制动画"""
        if not self.target_curve or self.target_curve.type != 'CURVE':
            return
        
        curve_data = self.target_curve.data
        
        # 移除动画数据
        if curve_data.animation_data and curve_data.animation_data.action:
            fcurves_to_remove = []
            for fcurve in curve_data.animation_data.action.fcurves:
                if fcurve.data_path in ["bevel_factor_start", "bevel_factor_end"]:
                    fcurves_to_remove.append(fcurve)
            
            for fcurve in fcurves_to_remove:
                curve_data.animation_data.action.fcurves.remove(fcurve)
        
        # 重置属性
        curve_data.bevel_factor_start = 0.0
        curve_data.bevel_factor_end = 1.0