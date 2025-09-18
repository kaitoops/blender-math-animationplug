import bpy
from ..core.error_handling import error_handler, PerformanceLevel

class MCPRenderOptimizer:
    """MCP动画渲染优化器，用于提升动作捕捉动画的渲染性能和视觉效果"""
    
    def __init__(self):
        self.armature = None
        self.original_settings = {}
        self.performance_level = PerformanceLevel.NORMAL
    
    def setup_render_optimization(self, armature, performance_level=PerformanceLevel.NORMAL):
        """设置渲染优化参数
        
        Args:
            armature: 骨骼装备对象
            performance_level: 性能级别，影响优化强度
        """
        try:
            self.armature = armature
            self.performance_level = performance_level
            
            # 保存原始设置
            self._backup_settings()
            
            # 应用优化设置
            self._apply_optimization_settings()
            
            return True
        except Exception as e:
            error_handler.handle_object_error(e, "Setting up render optimization")
            return False
    
    def restore_original_settings(self):
        """恢复原始渲染设置"""
        try:
            if not self.armature or not self.original_settings:
                return False
            
            # 恢复所有设置
            for attr, value in self.original_settings.items():
                setattr(self.armature, attr, value)
            
            # 清理状态
            self.armature = None
            self.original_settings.clear()
            
            return True
        except Exception as e:
            error_handler.handle_object_error(e, "Restoring original settings")
            return False
    
    def _backup_settings(self):
        """备份原始设置"""
        if not self.armature:
            return
        
        # 备份关键设置
        self.original_settings = {
            'show_in_front': self.armature.show_in_front,
            'display_type': self.armature.display_type,
            'show_names': self.armature.show_names,
            'show_axes': self.armature.show_axes
        }
    
    def _apply_optimization_settings(self):
        """应用优化设置"""
        if not self.armature:
            return
        
        # 基础优化设置
        self.armature.show_in_front = False
        self.armature.show_names = False
        self.armature.show_axes = False
        
        # 根据性能级别调整显示类型
        if self.performance_level == PerformanceLevel.HIGH:
            self.armature.display_type = 'STICK'
        elif self.performance_level == PerformanceLevel.NORMAL:
            self.armature.display_type = 'WIRE'
        else:
            self.armature.display_type = 'SOLID'
    
    def optimize_viewport_performance(self):
        """优化视窗性能"""
        try:
            if not self.armature:
                return False
            
            # 设置视窗优化选项
            context = bpy.context
            space = context.space_data
            
            if space and space.type == 'VIEW_3D':
                # 优化视窗显示设置
                space.show_object_viewport_mesh = False
                space.show_object_viewport_curve = False
                space.show_object_viewport_surf = False
                space.show_object_viewport_meta = False
                space.show_object_viewport_font = False
                space.show_object_viewport_pointcloud = False
                space.show_object_viewport_volume = False
                space.show_object_viewport_grease_pencil = False
                
                # 仅显示骨骼和必要对象
                space.show_object_viewport_armature = True
                
                return True
            
            return False
        except Exception as e:
            error_handler.handle_object_error(e, "Optimizing viewport performance")
            return False
    
    def optimize_render_settings(self, scene):
        """优化渲染设置
        
        Args:
            scene: 场景对象
        """
        try:
            render = scene.render
            
            # 根据性能级别优化渲染设置
            if self.performance_level == PerformanceLevel.HIGH:
                render.use_motion_blur = False
                render.use_shadows = False
                render.use_sss = False
                render.use_freestyle = False
            elif self.performance_level == PerformanceLevel.NORMAL:
                render.use_motion_blur = True
                render.use_shadows = True
                render.use_sss = False
                render.use_freestyle = False
            else:
                render.use_motion_blur = True
                render.use_shadows = True
                render.use_sss = True
                render.use_freestyle = True
            
            return True
        except Exception as e:
            error_handler.handle_object_error(e, "Optimizing render settings")
            return False