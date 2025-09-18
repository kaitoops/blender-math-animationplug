import bpy
import logging
from enum import Enum

class MathAnimError(Exception):
    """数学动画插件的基础异常类"""
    pass

class ObjectError(MathAnimError):
    """对象操作相关的异常"""
    pass

class SceneError(MathAnimError):
    """场景操作相关的异常"""
    pass

class PerformanceLevel(Enum):
    """性能日志级别"""
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"

class ErrorHandler:
    """错误处理和性能监控类"""
    
    def __init__(self):
        self.logger = logging.getLogger('math_anim')
        self.setup_logging()
    
    def setup_logging(self):
        """设置日志系统"""
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)
    
    def log_performance(self, level: PerformanceLevel, message: str):
        """记录性能相关的日志"""
        if level == PerformanceLevel.DEBUG:
            self.logger.debug(f"Performance: {message}")
        elif level == PerformanceLevel.INFO:
            self.logger.info(f"Performance: {message}")
        elif level == PerformanceLevel.WARNING:
            self.logger.warning(f"Performance: {message}")
        elif level == PerformanceLevel.ERROR:
            self.logger.error(f"Performance: {message}")
    
    def handle_object_error(self, error: Exception, context: str = ""):
        """处理对象操作相关的错误"""
        error_msg = f"Object operation error in {context}: {str(error)}"
        self.logger.error(error_msg)
        raise ObjectError(error_msg)
    
    def handle_scene_error(self, error: Exception, context: str = ""):
        """处理场景操作相关的错误"""
        error_msg = f"Scene operation error in {context}: {str(error)}"
        self.logger.error(error_msg)
        raise SceneError(error_msg)

# 创建全局错误处理器实例
error_handler = ErrorHandler()