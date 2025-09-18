import bpy
from bpy.props import FloatProperty, EnumProperty

class MeshSimplification(bpy.types.PropertyGroup):
    """网格简化工具，用于降低模型复杂度"""
    
    ratio = FloatProperty(
        name="Ratio",
        description="The ratio of faces to keep. 0.1 means 10% of original faces",
        default=0.5,
        min=0.0, max=1.0
    )
    
    method = EnumProperty(
        name="Method",
        description="Simplification algorithm",
        items=[
            ('COLLAPSE', 'Collapse', 'Collapse edges'),
            ('UNSUBDIV', 'Un-subdivide', 'Reverse a subdivision operation')
        ],
        default='COLLAPSE'
    )

    def apply(self, target_object):
        """对目标对象应用网格简化"""
        if not target_object or target_object.type != 'MESH':
            print("Target is not a mesh object.")
            return

        # 添加抽取修改器
        modifier = target_object.modifiers.new(name="MathMeshSimplification", type='DECIMATE')
        modifier.decimate_type = self.method
        
        if self.method == 'COLLAPSE':
            modifier.ratio = self.ratio
        elif self.method == 'UNSUBDIV':
            # Un-subdivide 需要迭代次数
            # 这里我们用一个基于比率的估算
            # 注意：这不是很精确
            import math
            iterations = int(math.log(1.0 / self.ratio, 4))
            modifier.iterations = max(0, iterations)

    def remove(self, target_object):
        """移除网格简化修改器"""
        if not target_object:
            return
            
        for mod in target_object.modifiers:
            if mod.name == "MathMeshSimplification":
                target_object.modifiers.remove(mod)