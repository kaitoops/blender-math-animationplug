import bpy
import numpy as np
from bpy.props import StringProperty, FloatVectorProperty, IntProperty, FloatProperty
from ..core.base import MathObjectBase

class Curve2D(MathObjectBase):
    """2D函数曲线类，支持参数方程和显式函数"""
    
    function = StringProperty(
        name="Function",
        description="Python expression for the function (use x as variable)",
        default="sin(x)"
    )
    
    domain = FloatVectorProperty(
        name="Domain",
        description="Function domain [min, max]",
        size=2,
        default=(-5.0, 5.0)
    )
    
    samples = IntProperty(
        name="Samples",
        description="Number of points to sample",
        default=100,
        min=10
    )
    
    thickness = FloatProperty(
        name="Thickness",
        description="Curve thickness",
        default=0.05,
        min=0.01
    )
    
    def create(self):
        """创建2D函数曲线"""
        # 生成采样点
        x = np.linspace(self.domain[0], self.domain[1], self.samples)
        try:
            # 创建安全的计算环境
            namespace = {
                'x': x,
                'sin': np.sin,
                'cos': np.cos,
                'tan': np.tan,
                'exp': np.exp,
                'log': np.log,
                'sqrt': np.sqrt,
                'pi': np.pi,
                'e': np.e
            }
            # 计算y值
            y = eval(self.function, {"__builtins__": {}}, namespace)
        except Exception as e:
            self.report({'ERROR'}, f"函数计算错误: {str(e)}")
            return
        
        # 创建曲线数据
        curve_data = bpy.data.curves.new(name="Function2D", type='CURVE')
        curve_data.dimensions = '3D'
        
        # 创建样条线
        polyline = curve_data.splines.new('POLY')
        polyline.points.add(len(x) - 1)
        
        # 设置点坐标
        for i, (px, py) in enumerate(zip(x, y)):
            polyline.points[i].co = (px, py, 0, 1)
        
        # 创建对象并设置属性
        self.obj = bpy.data.objects.new("Function2D", curve_data)
        
        # 设置曲线属性
        curve_data.bevel_depth = self.thickness
        curve_data.use_fill_caps = True
        
        # 创建材质
        mat = bpy.data.materials.new(name="Function2D_Material")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        
        # 清除默认节点
        nodes.clear()
        
        # 创建发射节点
        emission = nodes.new('ShaderNodeEmission')
        emission.inputs[0].default_value = (0.2, 0.8, 0.2, 1.0)  # 绿色
        emission.inputs[1].default_value = 2.0  # 强度
        
        # 创建输出节点
        output = nodes.new('ShaderNodeOutputMaterial')
        
        # 连接节点
        mat.node_tree.links.new(emission.outputs[0], output.inputs[0])
        
        # 分配材质
        self.obj.data.materials.append(mat)
    
    def update(self):
        """更新曲线属性和几何体"""
        if self.obj:
            curve_data = self.obj.data
            
            # 更新采样点
            x = np.linspace(self.domain[0], self.domain[1], self.samples)
            try:
                namespace = {
                    'x': x,
                    'sin': np.sin,
                    'cos': np.cos,
                    'tan': np.tan,
                    'exp': np.exp,
                    'log': np.log,
                    'sqrt': np.sqrt,
                    'pi': np.pi,
                    'e': np.e
                }
                y = eval(self.function, {"__builtins__": {}}, namespace)
            except Exception as e:
                self.report({'ERROR'}, f"函数计算错误: {str(e)}")
                return
            
            # 更新样条线点
            if len(curve_data.splines) > 0:
                spline = curve_data.splines[0]
                # 调整点数
                if len(spline.points) != len(x):
                    spline.points.add(len(x) - len(spline.points))
                
                # 更新点坐标
                for i, (px, py) in enumerate(zip(x, y)):
                    spline.points[i].co = (px, py, 0, 1)
            
            # 更新曲线属性
            curve_data.bevel_depth = self.thickness
    
    def delete(self):
        """删除曲线对象"""
        if self.obj:
            # 删除材质
            for mat in self.obj.data.materials:
                if mat:
                    bpy.data.materials.remove(mat)
            
            # 删除曲线数据
            curve_data = self.obj.data
            bpy.data.objects.remove(self.obj, do_unlink=True)
            bpy.data.curves.remove(curve_data)