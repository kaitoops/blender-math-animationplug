import bpy
from bpy.props import PointerProperty, StringProperty, FloatProperty, IntProperty

class FormulaEvolution(bpy.types.PropertyGroup):
    """公式演变动画类，使用文本序列"""
    
    target_text = PointerProperty(
        name="Target Text",
        description="Text object to animate",
        type=bpy.types.Object
    )
    
    formula_sequence = StringProperty(
        name="Formula Sequence",
        description="Comma-separated sequence of formulas to display",
        default="a, a+b, a+b=c"
    )
    
    start_frame = FloatProperty(
        name="Start Frame",
        description="Animation start frame",
        default=1.0
    )
    
    frame_step = IntProperty(
        name="Frame Step",
        description="Frames between each formula change",
        default=20,
        min=1
    )
    
    def apply(self):
        """应用公式演变动画"""
        if not self.target_text or self.target_text.type != 'FONT':
            return
        
        formulas = [f.strip() for f in self.formula_sequence.split(',')]
        
        current_frame = self.start_frame
        
        for i, formula in enumerate(formulas):
            # 设置文本内容
            self.target_text.data.body = formula
            # 插入关键帧
            self.target_text.data.keyframe_insert(data_path="body", frame=current_frame)
            
            # 保持到下一个关键帧之前
            if i < len(formulas) - 1:
                self.target_text.data.keyframe_insert(data_path="body", frame=current_frame + self.frame_step - 1)
            
            current_frame += self.frame_step
    
    def remove(self):
        """移除公式演变动画"""
        if not self.target_text or self.target_text.type != 'FONT':
            return
        
        if self.target_text.data.animation_data and self.target_text.data.animation_data.action:
            fcurves_to_remove = []
            for fcurve in self.target_text.data.animation_data.action.fcurves:
                if fcurve.data_path == "body":
                    fcurves_to_remove.append(fcurve)
            
            for fcurve in fcurves_to_remove:
                self.target_text.data.animation_data.action.fcurves.remove(fcurve)
        
        # 重置文本内容
        self.target_text.data.body = ""