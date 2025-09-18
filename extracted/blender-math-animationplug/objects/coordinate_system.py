import bpy
from bpy.props import FloatVectorProperty, FloatProperty, BoolProperty, EnumProperty
from ..core.base import MathObjectBase

class CoordinateSystem(MathObjectBase):
    """坐标系统类，支持2D/3D坐标轴和网格"""
    
    # 坐标系属性
    scale = FloatVectorProperty(
        name="Scale",
        description="Axis scale for each dimension",
        default=(1.0, 1.0, 1.0),
        min=0.0
    )
    
    grid_size = FloatProperty(
        name="Grid Size",
        description="Size of grid squares",
        default=1.0,
        min=0.1
    )
    
    show_grid = BoolProperty(
        name="Show Grid",
        description="Toggle grid visibility",
        default=True
    )
    
    dimension = EnumProperty(
        name="Dimension",
        description="Coordinate system dimension",
        items=[
            ('2D', '2D', 'Two-dimensional coordinate system'),
            ('3D', '3D', 'Three-dimensional coordinate system')
        ],
        default='3D'
    )
    
    def create(self):
        """创建坐标系几何体"""
        # 创建空物体作为坐标系容器
        self.obj = bpy.data.objects.new("CoordinateSystem", None)
        self.obj.empty_display_type = 'PLAIN_AXES'
        
        # 创建几何节点修改器
        modifier = self.obj.modifiers.new(name="CoordinateSystem", type='NODES')
        
        # 创建节点树
        node_tree = bpy.data.node_groups.new("CoordinateSystem", 'GeometryNodeTree')
        modifier.node_group = node_tree
        
        # 创建输入输出节点
        nodes = node_tree.nodes
        input_node = nodes.new('NodeGroupInput')
        output_node = nodes.new('NodeGroupOutput')
        
        # 创建轴线
        line_x = nodes.new('GeometryNodeCurveLine')
        line_y = nodes.new('GeometryNodeCurveLine')
        line_z = nodes.new('GeometryNodeCurveLine')
        
        # 设置轴线属性
        line_x.inputs[0].default_value = (-self.scale[0], 0, 0)
        line_x.inputs[1].default_value = (self.scale[0], 0, 0)
        
        line_y.inputs[0].default_value = (0, -self.scale[1], 0)
        line_y.inputs[1].default_value = (0, self.scale[1], 0)
        
        if self.dimension == '3D':
            line_z.inputs[0].default_value = (0, 0, -self.scale[2])
            line_z.inputs[1].default_value = (0, 0, self.scale[2])
        
        # 合并几何体
        join = nodes.new('GeometryNodeJoinGeometry')
        node_tree.links.new(line_x.outputs[0], join.inputs[0])
        node_tree.links.new(line_y.outputs[0], join.inputs[0])
        if self.dimension == '3D':
            node_tree.links.new(line_z.outputs[0], join.inputs[0])
        
        # 创建网格（如果启用）
        if self.show_grid:
            grid = nodes.new('GeometryNodeMeshGrid')
            grid.inputs['Size X'].default_value = self.scale[0] * 2
            grid.inputs['Size Y'].default_value = self.scale[1] * 2
            grid.inputs['Vertices X'].default_value = int(self.scale[0] / self.grid_size) * 2 + 1
            grid.inputs['Vertices Y'].default_value = int(self.scale[1] / self.grid_size) * 2 + 1
            
            # 将网格添加到合并节点
            node_tree.links.new(grid.outputs[0], join.inputs[0])
        
        # 连接输出
        node_tree.links.new(join.outputs[0], output_node.inputs[0])
    
    def update(self):
        """更新坐标系属性和几何体"""
        if self.obj and self.obj.modifiers:
            # 更新修改器属性
            modifier = self.obj.modifiers["CoordinateSystem"]
            if modifier:
                node_tree = modifier.node_group
                if node_tree:
                    # 更新节点属性
                    for node in node_tree.nodes:
                        if node.type == 'CURVE_LINE':
                            # 更新轴线
                            pass
                        elif node.type == 'MESH_GRID' and self.show_grid:
                            # 更新网格
                            node.inputs['Size X'].default_value = self.scale[0] * 2
                            node.inputs['Size Y'].default_value = self.scale[1] * 2
                            node.inputs['Vertices X'].default_value = int(self.scale[0] / self.grid_size) * 2 + 1
                            node.inputs['Vertices Y'].default_value = int(self.scale[1] / self.grid_size) * 2 + 1
    
    def delete(self):
        """删除坐标系对象"""
        if self.obj:
            # 删除节点树
            if self.obj.modifiers and "CoordinateSystem" in self.obj.modifiers:
                node_tree = self.obj.modifiers["CoordinateSystem"].node_group
                if node_tree:
                    bpy.data.node_groups.remove(node_tree)
            
            # 删除对象
            bpy.data.objects.remove(self.obj, do_unlink=True)