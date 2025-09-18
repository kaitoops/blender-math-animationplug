import bpy
import numpy as np
from bpy.props import StringProperty, FloatVectorProperty, IntProperty, FloatProperty, EnumProperty
from ..core.base import MathObjectBase

class Surface3D(MathObjectBase):
    """3D函数曲面类，支持显式函数和参数方程"""
    
    function_type = EnumProperty(
        name="Function Type",
        description="Function representation type",
        items=[
            ('EXPLICIT', 'Explicit', 'z = f(x,y)'),
            ('PARAMETRIC', 'Parametric', 'x=x(u,v), y=y(u,v), z=z(u,v)'),
            ('IMPLICIT', 'Implicit', 'f(x,y,z) = 0')
        ],
        default='EXPLICIT'
    )
    
    function_z = StringProperty(
        name="Z Function",
        description="Python expression for z (use x,y as variables)",
        default="sin(sqrt(x*x + y*y))"
    )
    
    function_x = StringProperty(
        name="X Function",
        description="Parametric X function (use u,v as variables)",
        default="u*cos(v)"
    )
    
    function_y = StringProperty(
        name="Y Function",
        description="Parametric Y function (use u,v as variables)",
        default="u*sin(v)"
    )
    
    domain_x = FloatVectorProperty(
        name="X Domain",
        description="X domain [min, max]",
        size=2,
        default=(-5.0, 5.0)
    )
    
    domain_y = FloatVectorProperty(
        name="Y Domain",
        description="Y domain [min, max]",
        size=2,
        default=(-5.0, 5.0)
    )
    
    resolution = IntProperty(
        name="Resolution",
        description="Grid resolution",
        default=50,
        min=10
    )
    
    def create(self):
        """创建3D函数曲面"""
        if self.function_type == 'EXPLICIT':
            self._create_explicit_surface()
        elif self.function_type == 'PARAMETRIC':
            self._create_parametric_surface()
        else:
            self.report({'ERROR'}, "暂不支持隐式函数")
    
    def _create_explicit_surface(self):
        """创建显式函数曲面"""
        # 生成网格点
        x = np.linspace(self.domain_x[0], self.domain_x[1], self.resolution)
        y = np.linspace(self.domain_y[0], self.domain_y[1], self.resolution)
        X, Y = np.meshgrid(x, y)
        
        try:
            # 创建安全的计算环境
            namespace = {
                'x': X,
                'y': Y,
                'sin': np.sin,
                'cos': np.cos,
                'tan': np.tan,
                'exp': np.exp,
                'log': np.log,
                'sqrt': np.sqrt,
                'pi': np.pi,
                'e': np.e
            }
            # 计算Z值
            Z = eval(self.function_z, {"__builtins__": {}}, namespace)
        except Exception as e:
            self.report({'ERROR'}, f"函数计算错误: {str(e)}")
            return
        
        # 创建网格数据
        vertices = []
        faces = []
        
        # 添加顶点
        for i in range(self.resolution):
            for j in range(self.resolution):
                vertices.append((X[i,j], Y[i,j], Z[i,j]))
        
        # 创建面
        for i in range(self.resolution-1):
            for j in range(self.resolution-1):
                idx = i * self.resolution + j
                faces.append((idx, idx+1, idx+self.resolution+1, idx+self.resolution))
        
        # 创建网格
        mesh = bpy.data.meshes.new(name="Surface3D")
        mesh.from_pydata(vertices, [], faces)
        mesh.update()
        
        # 创建对象
        self.obj = bpy.data.objects.new("Surface3D", mesh)
        
        # 添加材质
        self._create_surface_material()
    
    def _create_parametric_surface(self):
        """创建参数方程曲面"""
        # 生成参数网格
        u = np.linspace(self.domain_x[0], self.domain_x[1], self.resolution)
        v = np.linspace(self.domain_y[0], self.domain_y[1], self.resolution)
        U, V = np.meshgrid(u, v)
        
        try:
            # 创建安全的计算环境
            namespace = {
                'u': U,
                'v': V,
                'sin': np.sin,
                'cos': np.cos,
                'tan': np.tan,
                'exp': np.exp,
                'log': np.log,
                'sqrt': np.sqrt,
                'pi': np.pi,
                'e': np.e
            }
            # 计算X,Y,Z值
            X = eval(self.function_x, {"__builtins__": {}}, namespace)
            Y = eval(self.function_y, {"__builtins__": {}}, namespace)
            Z = eval(self.function_z, {"__builtins__": {}}, namespace)
        except Exception as e:
            self.report({'ERROR'}, f"函数计算错误: {str(e)}")
            return
        
        # 创建网格数据
        vertices = []
        faces = []
        
        # 添加顶点
        for i in range(self.resolution):
            for j in range(self.resolution):
                vertices.append((X[i,j], Y[i,j], Z[i,j]))
        
        # 创建面
        for i in range(self.resolution-1):
            for j in range(self.resolution-1):
                idx = i * self.resolution + j
                faces.append((idx, idx+1, idx+self.resolution+1, idx+self.resolution))
        
        # 创建网格
        mesh = bpy.data.meshes.new(name="Surface3D")
        mesh.from_pydata(vertices, [], faces)
        mesh.update()
        
        # 创建对象
        self.obj = bpy.data.objects.new("Surface3D", mesh)
        
        # 添加材质
        self._create_surface_material()
    
    def _create_surface_material(self):
        """创建曲面材质"""
        mat = bpy.data.materials.new(name="Surface3D_Material")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        
        # 清除默认节点
        nodes.clear()
        
        # 创建节点
        output = nodes.new('ShaderNodeOutputMaterial')
        principled = nodes.new('ShaderNodeBsdfPrincipled')
        gradient = nodes.new('ShaderNodeTexGradient')
        colorramp = nodes.new('ShaderNodeValToRGB')
        
        # 设置渐变颜色
        colorramp.color_ramp.elements[0].position = 0.0
        colorramp.color_ramp.elements[0].color = (0.0, 0.0, 1.0, 1.0)
        colorramp.color_ramp.elements[1].position = 1.0
        colorramp.color_ramp.elements[1].color = (1.0, 0.0, 0.0, 1.0)
        
        # 连接节点
        links.new(gradient.outputs[0], colorramp.inputs[0])
        links.new(colorramp.outputs[0], principled.inputs[0])
        links.new(principled.outputs[0], output.inputs[0])
        
        # 分配材质
        self.obj.data.materials.append(mat)
    
    def update(self):
        """更新曲面属性和几何体"""
        if self.obj:
            # 删除旧的几何体
            self.delete()
            # 重新创建
            self.create()
    
    def delete(self):
        """删除曲面对象"""
        if self.obj:
            # 删除材质
            for mat in self.obj.data.materials:
                if mat:
                    bpy.data.materials.remove(mat)
            
            # 删除网格数据
            mesh = self.obj.data
            bpy.data.objects.remove(self.obj, do_unlink=True)
            bpy.data.meshes.remove(mesh)