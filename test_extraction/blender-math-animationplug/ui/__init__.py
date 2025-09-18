import bpy

# 导入所有UI面板
from .object_panel import MATH_ANIM_PT_object_panel
from .animation_panel import MATH_ANIM_PT_animation_panel
from .render_panel import MATH_ANIM_PT_render_panel
from .performance_panel import MATH_ANIM_PT_performance_panel
from .workflow_panel import MATH_ANIM_PT_workflow_panel

_classes = [
    MATH_ANIM_PT_object_panel,
    MATH_ANIM_PT_animation_panel,
    MATH_ANIM_PT_render_panel,
    MATH_ANIM_PT_performance_panel,
    MATH_ANIM_PT_workflow_panel,
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)