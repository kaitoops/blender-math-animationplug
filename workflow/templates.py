import bpy
from bpy.props import EnumProperty

class TemplateManager(bpy.types.PropertyGroup):
    """一键模板，快速创建常见场景"""
    
    template = EnumProperty(
        name="Template",
        description="Select a scene template to create",
        items=[
            ('FRACTAL', 'Fractal', 'Create a fractal animation scene'),
            ('PHYSICS_SIM', 'Physics Simulation', 'Set up a basic physics simulation'),
            ('DATA_VIZ', 'Data Visualization', 'Create a data visualization setup')
        ],
        default='FRACTAL'
    )

    def apply_template(self):
        """根据所选模板创建场景"""
        # 清理当前场景
        self._clear_scene()
        
        if self.template == 'FRACTAL':
            self._create_fractal_template()
        elif self.template == 'PHYSICS_SIM':
            self._create_physics_sim_template()
        elif self.template == 'DATA_VIZ':
            self._create_data_viz_template()

    def _clear_scene(self):
        """清理场景中的所有对象、材质和动画"""
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        
        for material in bpy.data.materials:
            bpy.data.materials.remove(material)
            
        for curve in bpy.data.curves:
            bpy.data.curves.remove(curve)
            
        for mesh in bpy.data.meshes:
            bpy.data.meshes.remove(mesh)

    def _create_fractal_template(self):
        """创建分形动画模板"""
        # 创建一个平面作为几何节点的基础
        bpy.ops.mesh.primitive_plane_add()
        plane = bpy.context.active_object
        
        # 添加几何节点修改器
        gn_modifier = plane.modifiers.new(name="FractalNodes", type='NODES')
        node_group = bpy.data.node_groups.new("FractalTree", 'GeometryNodeTree')
        gn_modifier.node_group = node_group
        
        # (此处应添加复杂的分形节点逻辑)
        # ...
        print("Fractal template created (node setup is a placeholder).")

    def _create_physics_sim_template(self):
        """创建物理模拟模板"""
        # 创建一个地面
        bpy.ops.mesh.primitive_plane_add(size=20)
        ground = bpy.context.active_object
        ground.name = "Ground"
        bpy.ops.rigidbody.object_add(type='PASSIVE')
        
        # 创建一个立方体
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 5))
        cube = bpy.context.active_object
        cube.name = "FallingCube"
        bpy.ops.rigidbody.object_add(type='ACTIVE')
        
        print("Physics simulation template created.")

    def _create_data_viz_template(self):
        """创建数据可视化模板"""
        # 创建一个简单的条形图
        data = [5, 8, 3, 10, 6]
        for i, value in enumerate(data):
            bpy.ops.mesh.primitive_cube_add(location=(i * 2, 0, value / 2))
            bar = bpy.context.active_object
            bar.scale = (0.5, 0.5, value)
        
        print("Data visualization template created.")