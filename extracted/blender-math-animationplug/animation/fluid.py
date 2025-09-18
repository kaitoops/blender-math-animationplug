import bpy
from bpy.props import PointerProperty, FloatProperty, IntProperty, EnumProperty

class FluidAnimation(bpy.types.PropertyGroup):
    """流体动画类，使用粒子物理模拟流体"""
    
    domain_object = PointerProperty(
        name="Domain Object",
        description="Fluid simulation domain",
        type=bpy.types.Object
    )
    
    fluid_object = PointerProperty(
        name="Fluid Object",
        description="Object emitting the fluid",
        type=bpy.types.Object
    )
    
    resolution = IntProperty(
        name="Resolution",
        description="Simulation resolution",
        default=64,
        min=32
    )
    
    fluid_type = EnumProperty(
        name="Fluid Type",
        description="Type of fluid simulation",
        items=[
            ('GAS', 'Gas', 'Gas simulation (smoke, fire)'),
            ('LIQUID', 'Liquid', 'Liquid simulation')
        ],
        default='LIQUID'
    )
    
    start_frame = FloatProperty(
        name="Start Frame",
        description="Simulation start frame",
        default=1.0
    )
    
    end_frame = FloatProperty(
        name="End Frame",
        description="Simulation end frame",
        default=250.0
    )
    
    def apply(self):
        """应用流体动画设置"""
        if not self.domain_object or not self.fluid_object:
            return
        
        # 设置域对象
        domain_mod = self.domain_object.modifiers.new(name="Fluid", type='FLUID')
        domain_settings = domain_mod.fluid_settings
        domain_settings.type = 'DOMAIN'
        domain_settings.domain_type = self.fluid_type
        domain_settings.resolution_max = self.resolution
        
        # 设置流体对象
        fluid_mod = self.fluid_object.modifiers.new(name="Fluid", type='FLUID')
        fluid_settings = fluid_mod.fluid_settings
        fluid_settings.type = 'FLOW'
        fluid_settings.flow_type = 'INFLOW'
        fluid_settings.use_inflow = True
        
        # 设置场景帧范围
        bpy.context.scene.frame_start = int(self.start_frame)
        bpy.context.scene.frame_end = int(self.end_frame)
        
        # 烘焙模拟
        bpy.ops.fluid.bake_all()
    
    def remove(self):
        """移除流体动画设置"""
        # 移除域修改器
        if self.domain_object and "Fluid" in self.domain_object.modifiers:
            self.domain_object.modifiers.remove(self.domain_object.modifiers["Fluid"])
        
        # 移除流体修改器
        if self.fluid_object and "Fluid" in self.fluid_object.modifiers:
            self.fluid_object.modifiers.remove(self.fluid_object.modifiers["Fluid"])
        
        # 释放烘焙数据
        bpy.ops.fluid.free_all()