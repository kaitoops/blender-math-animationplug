import bpy
from bpy.props import EnumProperty

class StyleSwitcher(bpy.types.PropertyGroup):
    """一键切换整体视觉风格"""
    
    style: EnumProperty(
        name="Visual Style",
        description="Switch between different visual styles",
        items=[
            ('MODERN', 'Modern', 'Clean, modern look with realistic lighting'),
            ('WHITEBOARD', 'Whiteboard', 'Simulates a whiteboard animation style'),
            ('BLUEPRINT', 'Blueprint', 'Technical drawing/blueprint style')
        ],
        default='MODERN'
    )

    def apply(self):
        """应用所选的视觉风格"""
        if self.style == 'MODERN':
            self._apply_modern_style()
        elif self.style == 'WHITEBOARD':
            self._apply_whiteboard_style()
        elif self.style == 'BLUEPRINT':
            self._apply_blueprint_style()

    def _apply_modern_style(self):
        """应用现代风格"""
        # 设置背景
        bpy.context.scene.world.node_tree.nodes["Background"].inputs[0].default_value = (0.8, 0.8, 0.8, 1)
        
        # 移除NPR
        bpy.context.scene.render.use_freestyle = False
        
        # 设置灯光
        # (这里可以调用Lighting中的预设)

    def _apply_whiteboard_style(self):
        """应用白板风格"""
        # 白色背景
        bpy.context.scene.world.node_tree.nodes["Background"].inputs[0].default_value = (1, 1, 1, 1)
        
        # 开启NPR描边
        bpy.context.scene.render.use_freestyle = True
        freestyle_settings = bpy.context.scene.view_layers["ViewLayer"].freestyle_settings
        if not "MathNPRLineSet" in freestyle_settings.linesets:
            lineset = freestyle_settings.linesets.new("MathNPRLineSet")
        else:
            lineset = freestyle_settings.linesets["MathNPRLineSet"]
        lineset.linestyle.color = (0, 0, 0)
        lineset.select_border = True
        lineset.select_crease = False
        lineset.select_silhouette = True

    def _apply_blueprint_style(self):
        """应用蓝图风格"""
        # 蓝色背景
        bpy.context.scene.world.node_tree.nodes["Background"].inputs[0].default_value = (0.1, 0.2, 0.4, 1)
        
        # 白色描边
        bpy.context.scene.render.use_freestyle = True
        freestyle_settings = bpy.context.scene.view_layers["ViewLayer"].freestyle_settings
        if not "MathNPRLineSet" in freestyle_settings.linesets:
            lineset = freestyle_settings.linesets.new("MathNPRLineSet")
        else:
            lineset = freestyle_settings.linesets["MathNPRLineSet"]
        lineset.linestyle.color = (1, 1, 1)
        lineset.linestyle.thickness = 2
        lineset.select_border = True
        lineset.select_crease = True
        lineset.select_silhouette = True