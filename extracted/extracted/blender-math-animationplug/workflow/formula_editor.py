import bpy
from bpy.props import StringProperty

class FormulaEditor(bpy.types.PropertyGroup):
    """一个简单的公式编辑器，用于实时编辑LaTeX公式"""
    
    formula_text = StringProperty(
        name="Formula",
        description="Enter LaTeX formula here",
        default="e^{i\pi} + 1 = 0"
    )

    def draw(self, layout):
        """在UI中绘制公式编辑器"""
        layout.prop(self, "formula_text", text="")

    def apply_to_object(self, target_object):
        """将公式应用到选定的LaTeX对象"""
        if target_object and hasattr(target_object, 'math_object_properties') and target_object.math_object_properties.type == 'LATEX':
            target_object.math_object_properties.latex_formula.formula = self.formula_text
            # 触发更新
            target_object.math_object_properties.update_object(bpy.context)