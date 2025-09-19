import bpy
from bpy.props import BoolProperty, EnumProperty

class RealtimePreview(bpy.types.PropertyGroup):
    """实时预览设置，用于优化视口性能"""
    
    use_simplify: BoolProperty(
        name="Use Simplify",
        description="Enable global simplification for the viewport",
        default=False
    )
    
    display_mode: EnumProperty(
        name="Display Mode",
        description="How objects are displayed in the viewport",
        items=[
            ('SOLID', 'Solid', 'Display as solid'),
            ('WIREFRAME', 'Wireframe', 'Display as wireframe'),
            ('BOUNDS', 'Bounds', 'Display as bounding boxes')
        ],
        default='SOLID'
    )

    def apply(self):
        """应用实时预览设置"""
        scene = bpy.context.scene
        scene.render.use_simplify = self.use_simplify
        
        if self.use_simplify:
            # 降低细分级别
            scene.render.simplify_subdivision = 1
        
        # 设置所有对象的显示模式
        for obj in bpy.data.objects:
            if obj.type not in {'CAMERA', 'LIGHT'}:
                obj.display_type = self.display_mode

    def remove(self):
        """恢复默认预览设置"""
        scene = bpy.context.scene
        scene.render.use_simplify = False
        
        # 恢复所有对象的默认显示模式
        for obj in bpy.data.objects:
            if obj.type not in {'CAMERA', 'LIGHT'}:
                obj.display_type = 'TEXTURED' # 或者 'SOLID'