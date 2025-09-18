import bpy
from bpy.props import PointerProperty, CollectionProperty, StringProperty, BoolProperty, EnumProperty, FloatProperty, IntProperty

# 导入所有属性组类
from .render.material_system import MaterialSystem
from .render.lighting import Lighting
from .render.npr_render import NPRRender
from .render.special_effects import SpecialEffects
from .render.style_switcher import StyleSwitcher

from .performance.realtime_preview import RealtimePreview
from .performance.mesh_simplification import MeshSimplification
from .performance.gpu_acceleration import GPUAcceleration
from .performance.batch_export import BatchExport

from .workflow.templates import TemplateManager
from .workflow.formula_editor import FormulaEditor
from .workflow.error_diagnostic import ErrorDiagnostic
from .workflow.interactive_tutorial import InteractiveTutorial

from .mcp.animation_controller import MCPAnimationController

# 渲染模块属性组
class MathAnimRenderProperties(bpy.types.PropertyGroup):
    """渲染模块属性组"""
    material: PointerProperty(type=MaterialSystem)
    lighting: PointerProperty(type=Lighting)
    npr: PointerProperty(type=NPRRender)
    effects: PointerProperty(type=SpecialEffects)
    style: PointerProperty(type=StyleSwitcher)

# 性能模块属性组
class MathAnimPerformanceProperties(bpy.types.PropertyGroup):
    """性能模块属性组"""
    realtime_preview: PointerProperty(type=RealtimePreview)
    mesh_simplification: PointerProperty(type=MeshSimplification)
    gpu_acceleration: PointerProperty(type=GPUAcceleration)
    batch_export: PointerProperty(type=BatchExport)

# 工作流模块属性组
class MathAnimWorkflowProperties(bpy.types.PropertyGroup):
    """工作流模块属性组"""
    templates: PointerProperty(type=TemplateManager)
    formula_editor: PointerProperty(type=FormulaEditor)
    error_diagnostic: PointerProperty(type=ErrorDiagnostic)
    interactive_tutorial: PointerProperty(type=InteractiveTutorial)

# MCP模块属性组
class MathAnimMCPProperties(bpy.types.PropertyGroup):
    """MCP模块属性组"""
    controller: PointerProperty(type=MCPAnimationController)

# 主属性组
class MathAnimProperties(bpy.types.PropertyGroup):
    """数学动画插件的主属性组"""
    render: PointerProperty(type=MathAnimRenderProperties)
    performance: PointerProperty(type=MathAnimPerformanceProperties)
    workflow: PointerProperty(type=MathAnimWorkflowProperties)
    mcp: PointerProperty(type=MathAnimMCPProperties)

def register():
    # 注册所有属性类
    bpy.utils.register_class(MaterialSystem)
    bpy.utils.register_class(Lighting)
    bpy.utils.register_class(NPRRender)
    bpy.utils.register_class(SpecialEffects)
    bpy.utils.register_class(StyleSwitcher)
    
    bpy.utils.register_class(RealtimePreview)
    bpy.utils.register_class(MeshSimplification)
    bpy.utils.register_class(GPUAcceleration)
    bpy.utils.register_class(BatchExport)
    
    bpy.utils.register_class(TemplateManager)
    bpy.utils.register_class(FormulaEditor)
    bpy.utils.register_class(ErrorDiagnostic)
    bpy.utils.register_class(InteractiveTutorial)
    
    bpy.utils.register_class(MCPAnimationController)
    
    bpy.utils.register_class(MathAnimRenderProperties)
    bpy.utils.register_class(MathAnimPerformanceProperties)
    bpy.utils.register_class(MathAnimWorkflowProperties)
    bpy.utils.register_class(MathAnimMCPProperties)
    bpy.utils.register_class(MathAnimProperties)
    
    # 将主属性组添加到Scene类型
    bpy.types.Scene.math_anim_properties = PointerProperty(type=MathAnimProperties)

def unregister():
    # 删除Scene上的属性引用
    del bpy.types.Scene.math_anim_properties
    
    # 按相反顺序注销类
    bpy.utils.unregister_class(MathAnimProperties)
    bpy.utils.unregister_class(MathAnimMCPProperties)
    bpy.utils.unregister_class(MathAnimWorkflowProperties)
    bpy.utils.unregister_class(MathAnimPerformanceProperties)
    bpy.utils.unregister_class(MathAnimRenderProperties)
    
    bpy.utils.unregister_class(MCPAnimationController)
    
    bpy.utils.unregister_class(InteractiveTutorial)
    bpy.utils.unregister_class(ErrorDiagnostic)
    bpy.utils.unregister_class(FormulaEditor)
    bpy.utils.unregister_class(TemplateManager)
    
    bpy.utils.unregister_class(BatchExport)
    bpy.utils.unregister_class(GPUAcceleration)
    bpy.utils.unregister_class(MeshSimplification)
    bpy.utils.unregister_class(RealtimePreview)
    
    bpy.utils.unregister_class(StyleSwitcher)
    bpy.utils.unregister_class(SpecialEffects)
    bpy.utils.unregister_class(NPRRender)
    bpy.utils.unregister_class(Lighting)
    bpy.utils.unregister_class(MaterialSystem)