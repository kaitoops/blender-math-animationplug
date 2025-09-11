import unittest
import sys
import os
import bpy

# 添加项目根目录到Python路径
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

# 导入测试模块
from tests.test_mcp import (
    TestMCPDataProcessor,
    TestMCPWorkflowManager,
    TestMCPRenderOptimizer,
    TestMCPAnimationController
)

def run_tests():
    # 创建测试套件
    test_suite = unittest.TestSuite()
    
    # 添加MCP模块的测试用例
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMCPDataProcessor))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMCPWorkflowManager))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMCPRenderOptimizer))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMCPAnimationController))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # 返回测试结果
    return result.wasSuccessful()

if __name__ == "__main__":
    # 设置Blender环境
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    
    # 运行测试
    success = run_tests()
    
    # 根据测试结果设置退出码
    sys.exit(0 if success else 1)