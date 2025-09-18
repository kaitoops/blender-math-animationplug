import bpy
from bpy.props import PointerProperty, CollectionProperty

# 在这里定义属性组，而不是导入其他模块的类
# 因为这样会造成循环导入问题

class MathAnimMCPProperties(bpy.types.PropertyGroup):
    """MCP模块属性"""
    pass

class MathAnimProperties(bpy.types.PropertyGroup):
    """数学动画插件的主属性组"""
    
    # MCP模块属性
    mcp: PointerProperty(type=MathAnimMCPProperties)

def register():
    bpy.utils.register_class(MathAnimMCPProperties)
    bpy.utils.register_class(MathAnimProperties)
    # 将属性组添加到Scene类型
    bpy.types.Scene.math_anim_properties = PointerProperty(type=MathAnimProperties)

def unregister():
    del bpy.types.Scene.math_anim_properties
    bpy.utils.unregister_class(MathAnimProperties)
    bpy.utils.unregister_class(MathAnimMCPProperties)