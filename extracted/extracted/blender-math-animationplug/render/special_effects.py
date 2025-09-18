import bpy
from bpy.props import BoolProperty, FloatProperty

class SpecialEffects(bpy.types.PropertyGroup):
    """后期处理特效"""
    
    use_bloom = BoolProperty(
        name="Use Bloom",
        description="Enable bloom effect for emissive materials",
        default=False
    )
    
    bloom_intensity = FloatProperty(
        name="Bloom Intensity",
        description="Intensity of the bloom effect",
        default=0.05,
        min=0.0
    )
    
    use_motion_blur = BoolProperty(
        name="Use Motion Blur",
        description="Enable motion blur for moving objects",
        default=False
    )

    def apply(self):
        """应用后期特效"""
        scene = bpy.context.scene
        
        # Eevee 渲染器设置
        if scene.render.engine == 'BLENDER_EEVEE':
            scene.eevee.use_bloom = self.use_bloom
            scene.eevee.bloom_intensity = self.bloom_intensity
        
        # Cycles 和 Eevee 通用设置
        scene.render.use_motion_blur = self.use_motion_blur

    def remove(self):
        """移除后期特效"""
        scene = bpy.context.scene
        
        if scene.render.engine == 'BLENDER_EEVEE':
            scene.eevee.use_bloom = False
        
        scene.render.use_motion_blur = False