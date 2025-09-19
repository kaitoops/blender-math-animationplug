import bpy
from bpy.props import BoolProperty

class GPUAcceleration(bpy.types.PropertyGroup):
    """GPU加速设置"""
    
    use_gpu: BoolProperty(
        name="Use GPU for Rendering",
        description="Enable GPU for Cycles rendering if available",
        default=False
    )

    def apply(self):
        """尝试启用GPU渲染"""
        scene = bpy.context.scene
        if self.use_gpu and scene.render.engine == 'CYCLES':
            # 检查CUDA或OptiX设备
            prefs = bpy.context.preferences.addons['cycles'].preferences
            prefs.compute_device_type = 'CUDA' # 或者 'OPTIX'
            
            # 激活所有可用的GPU
            prefs.get_devices()
            for device in prefs.devices:
                if device.type == 'CUDA' or device.type == 'OPTIX':
                    device.use = True
            
            scene.cycles.device = 'GPU'
            print("GPU rendering enabled.")
        else:
            # 回到CPU
            scene.cycles.device = 'CPU'
            print("Rendering with CPU.")

    def remove(self):
        """禁用GPU渲染，切换回CPU"""
        scene = bpy.context.scene
        if scene.render.engine == 'CYCLES':
            scene.cycles.device = 'CPU'