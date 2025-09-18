import bpy
import numpy as np
from bpy.props import EnumProperty, FloatProperty, IntProperty
from ..core.base import MathObjectBase

class ProbabilityDistribution(MathObjectBase):
    """概率分布可视化类，支持正态分布和均匀分布"""
    
    dist_type = EnumProperty(
        name="Distribution Type",
        description="Type of probability distribution",
        items=[
            ('NORMAL', 'Normal', 'Normal (Gaussian) distribution'),
            ('UNIFORM', 'Uniform', 'Uniform distribution')
        ],
        default='NORMAL'
    )
    
    mean = FloatProperty(
        name="Mean (μ)",
        description="Mean of the normal distribution",
        default=0.0
    )
    
    std_dev = FloatProperty(
        name="Standard Deviation (σ)",
        description="Standard deviation of the normal distribution",
        default=1.0,
        min=0.1
    )
    
    range_min = FloatProperty(
        name="Range Min",
        description="Minimum value for uniform distribution",
        default=-1.0
    )
    
    range_max = FloatProperty(
        name="Range Max",
        description="Maximum value for uniform distribution",
        default=1.0
    )
    
    samples = IntProperty(
        name="Samples",
        description="Number of points to sample for the curve",
        default=200,
        min=20
    )
    
    def create(self):
        """创建概率分布曲线"""
        # 创建曲线数据
        curve_data = bpy.data.curves.new(name="ProbabilityDistribution", type='CURVE')
        curve_data.dimensions = '2D'
        
        # 创建样条线
        polyline = curve_data.splines.new('POLY')
        
        # 生成数据点
        if self.dist_type == 'NORMAL':
            x = np.linspace(self.mean - 4*self.std_dev, self.mean + 4*self.std_dev, self.samples)
            y = (1 / (self.std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - self.mean) / self.std_dev)**2)
        else: # UNIFORM
            x = np.linspace(self.range_min - 0.5, self.range_max + 0.5, self.samples)
            y = np.where((x >= self.range_min) & (x <= self.range_max), 1 / (self.range_max - self.range_min), 0)
        
        # 添加点到样条线
        polyline.points.add(len(x) - 1)
        for i, (px, py) in enumerate(zip(x, y)):
            polyline.points[i].co = (px, py, 0, 1)
            
        # 创建对象
        self.obj = bpy.data.objects.new("ProbabilityDistribution", curve_data)
        
        # 创建材质
        self._create_distribution_material()
    
    def _create_distribution_material(self):
        """创建分布曲线材质"""
        mat = bpy.data.materials.new(name="Distribution_Material")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        
        # 清除默认节点
        nodes.clear()
        
        # 创建节点
        output = nodes.new('ShaderNodeOutputMaterial')
        emission = nodes.new('ShaderNodeEmission')
        
        # 设置颜色和强度
        emission.inputs[0].default_value = (0.8, 0.2, 0.8, 1.0) # 紫色
        emission.inputs[1].default_value = 2.0
        
        # 连接节点
        links.new(emission.outputs[0], output.inputs[0])
        
        # 分配材质
        self.obj.data.materials.append(mat)

    def update(self):
        """更新分布曲线"""
        if self.obj:
            curve_data = self.obj.data
            spline = curve_data.splines[0]
            
            # 重新生成数据点
            if self.dist_type == 'NORMAL':
                x = np.linspace(self.mean - 4*self.std_dev, self.mean + 4*self.std_dev, self.samples)
                y = (1 / (self.std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - self.mean) / self.std_dev)**2)
            else: # UNIFORM
                x = np.linspace(self.range_min - 0.5, self.range_max + 0.5, self.samples)
                y = np.where((x >= self.range_min) & (x <= self.range_max), 1 / (self.range_max - self.range_min), 0)
            
            # 更新样条线点
            if len(spline.points) != len(x):
                spline.points.add(len(x) - len(spline.points))
            
            for i, (px, py) in enumerate(zip(x, y)):
                spline.points[i].co = (px, py, 0, 1)

    def delete(self):
        """删除分布对象"""
        if self.obj:
            # 删除材质
            for mat in self.obj.data.materials:
                if mat:
                    bpy.data.materials.remove(mat)
            
            # 删除曲线数据
            curve_data = self.obj.data
            bpy.data.objects.remove(self.obj, do_unlink=True)
            bpy.data.curves.remove(curve_data)