import bpy
import numpy as np
from bpy.props import StringProperty, FloatVectorProperty, IntProperty, FloatProperty, BoolProperty
from ..core.base import MathObjectBase

class VectorField(MathObjectBase):
    """向量场可视化类，使用粒子系统展示向量场"""
    
    function_x = StringProperty(
        name="X Component",
        description="X component of vector field (use x,y,z as variables)",
        default="-y"
    )
    
    function_y = StringProperty(
        name="Y Component",
        description="Y component of vector field (use x,y,z as variables)",
        default="x"
    )
    
    function_z = StringProperty(
        name="Z Component",
        description="Z component of vector field (use x,y,z as variables)",
        default="0"
    )
    
    domain = FloatVectorProperty(
        name="Domain",
        description="Field domain size",
        size=3,
        default=(-5.0, 5.0, -5.0, 5.0, -5.0, 5.0)
    )
    
    particles_per_dim = IntProperty(
        name="Particles per Dimension",
        description="Number of particles per dimension",
        default=10,
        min=5
    )
    
    arrow_scale = FloatProperty(
        name="Arrow Scale",
        description="Scale factor for arrows",
        default=1.0,
        min=0.1
    )
    
    animate = BoolProperty(
        name="Animate",
        description="Animate particles along field lines",
        default=False
    )
    
    def create(self):
        """创建向量场可视化"""
        # 创建粒子发射器网格
        bpy.ops.mesh.primitive_grid_add(
            size=1,
            x_subdivisions=self.particles_per_dim,
            y_subdivisions=self.particles_per_dim
        )
        emitter = bpy.context.active_object
        
        # 缩放和定位发射器
        emitter.scale = (
            (self.domain[1] - self.domain[0])/2,
            (self.domain[3] - self.domain[2])/2,
            1
        )
        emitter.location = (
            (self.domain[1] + self.domain[0])/2,
            (self.domain[3] + self.domain[2])/2,
            self.domain[4]
        )
        
        # 创建粒子系统
        particle_sys = emitter.modifiers.new(name="VectorField", type='PARTICLE_SYSTEM')
        settings = particle_sys.particle_system.settings
        
        # 配置粒子系统
        settings.type = 'HAIR'
        settings.count = self.particles_per_dim * self.particles_per_dim
        settings.hair_length = self.arrow_scale
        settings.use_advanced_hair = True
        
        if self.animate:
            settings.physics_type = 'NEWTON'
            settings.particle_size = 0.1
            settings.lifetime = 100
            settings.frame_start = 1
            settings.frame_end = 1
            settings.normal_factor = 0
        
        # 创建自定义属性驱动向量场
        emitter["field_x"] = self.function_x
        emitter["field_y"] = self.function_y
        emitter["field_z"] = self.function_z
        
        # 创建驱动器更新粒子方向
        self._setup_field_drivers(emitter)
        
        # 保存对象引用
        self.obj = emitter
        
        # 创建材质
        self._create_particle_material()
    
    def _setup_field_drivers(self, obj):
        """设置向量场驱动器"""
        # 创建驱动器命名空间
        namespace = {
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'exp': np.exp,
            'log': np.log,
            'sqrt': np.sqrt,
            'pi': np.pi,
            'e': np.e
        }
        
        # 为每个粒子创建驱动器
        psys = obj.particle_systems[0]
        for p in psys.particles:
            # 获取粒子位置
            loc = p.location
            
            # 计算向量场在该点的值
            try:
                x = eval(self.function_x.replace('x', str(loc.x)).replace('y', str(loc.y)).replace('z', str(loc.z)),
                         {"__builtins__": {}}, namespace)
                y = eval(self.function_y.replace('x', str(loc.x)).replace('y', str(loc.y)).replace('z', str(loc.z)),
                         {"__builtins__": {}}, namespace)
                z = eval(self.function_z.replace('x', str(loc.x)).replace('y', str(loc.y)).replace('z', str(loc.z)),
                         {"__builtins__": {}}, namespace)
                
                # 设置粒子速度/方向
                magnitude = np.sqrt(x*x + y*y + z*z)
                if magnitude > 0:
                    p.velocity = (x/magnitude, y/magnitude, z/magnitude)
                    p.hair_length = magnitude * self.arrow_scale
            except Exception as e:
                self.report({'ERROR'}, f"向量场计算错误: {str(e)}")
    
    def _create_particle_material(self):
        """创建粒子材质"""
        mat = bpy.data.materials.new(name="VectorField_Material")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        
        # 清除默认节点
        nodes.clear()
        
        # 创建节点
        output = nodes.new('ShaderNodeOutputMaterial')
        emission = nodes.new('ShaderNodeEmission')
        colorramp = nodes.new('ShaderNodeValToRGB')
        vector = nodes.new('ShaderNodeVectorMath')
        
        # 设置节点属性
        vector.operation = 'LENGTH'
        emission.inputs[1].default_value = 2.0  # 发光强度
        
        # 设置颜色渐变
        colorramp.color_ramp.elements[0].position = 0.0
        colorramp.color_ramp.elements[0].color = (0.0, 0.0, 1.0, 1.0)  # 蓝色
        colorramp.color_ramp.elements[1].position = 1.0
        colorramp.color_ramp.elements[1].color = (1.0, 0.0, 0.0, 1.0)  # 红色
        
        # 连接节点
        links.new(vector.outputs[1], colorramp.inputs[0])
        links.new(colorramp.outputs[0], emission.inputs[0])
        links.new(emission.outputs[0], output.inputs[0])
        
        # 分配材质
        self.obj.data.materials.append(mat)
    
    def update(self):
        """更新向量场属性和可视化"""
        if self.obj:
            # 更新发射器属性
            self.obj.scale = (
                (self.domain[1] - self.domain[0])/2,
                (self.domain[3] - self.domain[2])/2,
                1
            )
            self.obj.location = (
                (self.domain[1] + self.domain[0])/2,
                (self.domain[3] + self.domain[2])/2,
                self.domain[4]
            )
            
            # 更新粒子系统
            if len(self.obj.particle_systems) > 0:
                settings = self.obj.particle_systems[0].settings
                settings.count = self.particles_per_dim * self.particles_per_dim
                settings.hair_length = self.arrow_scale
                
                # 更新向量场函数
                self.obj["field_x"] = self.function_x
                self.obj["field_y"] = self.function_y
                self.obj["field_z"] = self.function_z
                
                # 重新计算粒子方向
                self._setup_field_drivers(self.obj)
    
    def delete(self):
        """删除向量场对象"""
        if self.obj:
            # 删除材质
            for mat in self.obj.data.materials:
                if mat:
                    bpy.data.materials.remove(mat)
            
            # 删除网格数据
            mesh = self.obj.data
            bpy.data.objects.remove(self.obj, do_unlink=True)
            bpy.data.meshes.remove(mesh)