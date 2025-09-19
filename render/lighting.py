import bpy
from bpy.props import EnumProperty, FloatProperty

class Lighting(bpy.types.PropertyGroup):
    """灯光系统，用于创建和管理灯光"""
    
    preset: EnumProperty(
        name="Preset",
        description="Select a lighting preset",
        items=[
            ('THREE_POINT', 'Three-Point', 'Standard three-point lighting'),
            ('RIM', 'Rim Light', 'Backlight for highlighting edges'),
            ('AMBIENT', 'Ambient', 'Soft, global illumination')
        ],
        default='THREE_POINT'
    )
    
    intensity: FloatProperty(
        name="Intensity",
        description="Overall light intensity multiplier",
        default=1.0,
        min=0.0
    )

    def apply(self, target_object):
        """在场景中应用灯光预设"""
        self.remove() # 移除旧的灯光
        
        if self.preset == 'THREE_POINT':
            self._create_three_point_lighting(target_object)
        elif self.preset == 'RIM':
            self._create_rim_light(target_object)
        elif self.preset == 'AMBIENT':
            self._create_ambient_light()

    def remove(self):
        """移除此系统创建的所有灯光"""
        for obj in bpy.data.objects:
            if obj.name.startswith("MathLight_"):
                bpy.data.objects.remove(obj, do_unlink=True)

    def _create_three_point_lighting(self, target):
        """创建标准三点光"""
        # 主光源 (Key Light)
        key_light = bpy.data.lights.new(name="MathLight_Key", type='AREA')
        key_light.energy = 100 * self.intensity
        key_obj = bpy.data.objects.new(name="MathLight_Key", object_data=key_light)
        key_obj.location = (target.location.x - 5, target.location.y - 5, target.location.z + 5)
        bpy.context.collection.objects.link(key_obj)

        # 辅助光 (Fill Light)
        fill_light = bpy.data.lights.new(name="MathLight_Fill", type='AREA')
        fill_light.energy = 50 * self.intensity
        fill_obj = bpy.data.objects.new(name="MathLight_Fill", object_data=fill_light)
        fill_obj.location = (target.location.x + 5, target.location.y - 5, target.location.z + 2)
        bpy.context.collection.objects.link(fill_obj)

        # 轮廓光 (Back Light)
        back_light = bpy.data.lights.new(name="MathLight_Back", type='AREA')
        back_light.energy = 75 * self.intensity
        back_obj = bpy.data.objects.new(name="MathLight_Back", object_data=back_light)
        back_obj.location = (target.location.x, target.location.y + 5, target.location.z + 3)
        bpy.context.collection.objects.link(back_obj)

    def _create_rim_light(self, target):
        """创建轮廓光"""
        rim_light = bpy.data.lights.new(name="MathLight_Rim", type='SPOT')
        rim_light.energy = 200 * self.intensity
        rim_obj = bpy.data.objects.new(name="MathLight_Rim", object_data=rim_light)
        rim_obj.location = (target.location.x, target.location.y + 6, target.location.z + 4)
        
        # 将聚光灯指向目标
        track_to = rim_obj.constraints.new(type='TRACK_TO')
        track_to.target = target
        track_to.track_axis = 'TRACK_NEGATIVE_Z'
        track_to.up_axis = 'UP_Y'
        
        bpy.context.collection.objects.link(rim_obj)

    def _create_ambient_light(self):
        """创建环境光"""
        world = bpy.context.scene.world
        world.use_nodes = True
        bg_node = world.node_tree.nodes.get('Background')
        if bg_node:
            bg_node.inputs['Color'].default_value = (0.1, 0.1, 0.1, 1)
            bg_node.inputs['Strength'].default_value = 1.0 * self.intensity