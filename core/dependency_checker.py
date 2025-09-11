import bpy
import addon_utils

class DependencyChecker:
    """检查和管理插件依赖项"""
    
    REQUIRED_ADDONS = {
        'images_as_planes': {
            'name': 'Import Images as Planes',
            'description': '用于LaTeX公式渲染',
            'required': True
        },
        'node_wrangler': {
            'name': 'Node Wrangler',
            'description': '用于几何节点编程',
            'required': True
        },
        'sverchok': {
            'name': 'Sverchok',
            'description': '用于高级3D函数曲面',
            'required': False
        }
    }
    
    @classmethod
    def check_dependencies(cls):
        """检查所有依赖项的状态"""
        missing_required = []
        missing_optional = []
        
        for addon_id, info in cls.REQUIRED_ADDONS.items():
            if not cls.is_addon_enabled(addon_id):
                if info['required']:
                    missing_required.append(info['name'])
                else:
                    missing_optional.append(info['name'])
        
        if missing_required:
            cls.show_missing_dependencies_warning(missing_required, True)
        
        if missing_optional:
            cls.show_missing_dependencies_warning(missing_optional, False)
    
    @staticmethod
    def is_addon_enabled(addon_id):
        """检查插件是否已启用"""
        return addon_utils.check(addon_id)[1]
    
    @staticmethod
    def enable_addon(addon_id):
        """启用指定插件"""
        try:
            addon_utils.enable(addon_id, default_set=True, persistent=True)
            return True
        except:
            return False
    
    @staticmethod
    def show_missing_dependencies_warning(missing_addons, required=True):
        """显示依赖缺失警告"""
        message = "缺少{}插件:\n".format("必需" if required else "可选")
        message += "\n".join(["- " + addon for addon in missing_addons])
        
        def draw(self, context):
            self.layout.label(text=message)
        
        bpy.context.window_manager.popup_menu(draw, 
            title="依赖检查", 
            icon='ERROR' if required else 'INFO')
    
    @classmethod
    def install_dependencies(cls):
        """尝试安装和启用所有必需的依赖项"""
        for addon_id, info in cls.REQUIRED_ADDONS.items():
            if info['required'] and not cls.is_addon_enabled(addon_id):
                if not cls.enable_addon(addon_id):
                    cls.show_missing_dependencies_warning([info['name']], True)