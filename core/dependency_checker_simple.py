import bpy
import addon_utils

class DependencyChecker:
    """简化版依赖检查器"""
    
    @classmethod
    def check_dependencies(cls):
        """检查依赖项 - 简化版，只检查最基本的依赖"""
        try:
            # 检查基本的Blender模块
            import mathutils
            import bmesh
            
            # 检查是否能导入基本模块
            from ..objects.operators import AddCoordinateSystemOperator
            
            print("✓ 基本依赖检查通过")
            return True
        except ImportError as e:
            print(f"✗ 依赖检查失败: {e}")
            return False
        except Exception as e:
            print(f"✗ 依赖检查出现错误: {e}")
            return False
    
    @classmethod
    def install_dependencies(cls):
        """安装依赖项 - 简化版"""
        # 在简化版中不执行任何操作
        return True