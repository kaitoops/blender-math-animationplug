import bpy
from bpy.props import BoolProperty, FloatVectorProperty

class NPRRender(bpy.types.PropertyGroup):
    """NPR（非真实感渲染）设置"""
    
    use_outline: BoolProperty(
        name="Use Outline",
        description="Enable freestyle outlines for a comic book look",
        default=False
    )
    
    outline_color: FloatVectorProperty(
        name="Outline Color",
        description="Color of the outlines",
        subtype='COLOR',
        default=(0.0, 0.0, 0.0),
        min=0.0,
        max=1.0
    )

    def apply(self):
        """应用NPR设置"""
        bpy.context.scene.render.use_freestyle = self.use_outline
        
        if self.use_outline:
            freestyle_settings = bpy.context.scene.view_layers["ViewLayer"].freestyle_settings
            lineset = freestyle_settings.linesets.new("MathNPRLineSet")
            
            # 设置线条颜色
            lineset.linestyle.color = self.outline_color
            
            # 选择要渲染的线条类型
            lineset.select_border = True
            lineset.select_crease = True
            lineset.select_silhouette = True

    def remove(self):
        """移除NPR设置"""
        bpy.context.scene.render.use_freestyle = False
        
        # 移除我们创建的线条集
        freestyle_settings = bpy.context.scene.view_layers["ViewLayer"].freestyle_settings
        for lineset in freestyle_settings.linesets:
            if lineset.name == "MathNPRLineSet":
                freestyle_settings.linesets.remove(lineset)