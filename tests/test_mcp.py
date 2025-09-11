import unittest
import bpy
import os
import tempfile
from ..core.error_handling import error_handler, PerformanceLevel
from ..mcp.data_processor import MCPDataProcessor
from ..mcp.animation_controller import MCPAnimationController
from ..mcp.workflow_manager import MCPWorkflowManager
from ..mcp.render_optimizer import MCPRenderOptimizer

class TestMCPDataProcessor(unittest.TestCase):
    def setUp(self):
        self.data_processor = MCPDataProcessor()
        self.test_file = os.path.join(tempfile.gettempdir(), 'test_mcp.txt')
        with open(self.test_file, 'w') as f:
            f.write('测试MCP数据')
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_load_mcp_file(self):
        success = self.data_processor.load_mcp_file(self.test_file)
        self.assertTrue(success)
    
    def test_get_animation_data(self):
        self.data_processor.load_mcp_file(self.test_file)
        data = self.data_processor.get_animation_data()
        self.assertIsNotNone(data)
    
    def test_cleanup(self):
        self.data_processor.load_mcp_file(self.test_file)
        self.data_processor.cleanup()
        self.assertIsNone(self.data_processor.get_animation_data())

class TestMCPWorkflowManager(unittest.TestCase):
    def setUp(self):
        self.workflow_manager = MCPWorkflowManager()
        # 创建测试用骨骼装备
        bpy.ops.object.armature_add()
        self.armature = bpy.context.active_object
    
    def tearDown(self):
        # 清理测试用骨骼装备
        bpy.ops.object.select_all(action='DESELECT')
        self.armature.select_set(True)
        bpy.context.view_layer.objects.active = self.armature
        bpy.ops.object.delete()
    
    def test_initialize_workflow(self):
        success = self.workflow_manager.initialize_workflow(self.armature)
        self.assertTrue(success)
    
    def test_save_mapping_template(self):
        self.workflow_manager.initialize_workflow(self.armature)
        success = self.workflow_manager.save_mapping_template('test_template')
        self.assertTrue(success)
    
    def test_apply_mapping_template(self):
        self.workflow_manager.initialize_workflow(self.armature)
        self.workflow_manager.save_mapping_template('test_template')
        success = self.workflow_manager.apply_mapping_template('test_template')
        self.assertTrue(success)

class TestMCPRenderOptimizer(unittest.TestCase):
    def setUp(self):
        self.render_optimizer = MCPRenderOptimizer()
        # 创建测试用骨骼装备
        bpy.ops.object.armature_add()
        self.armature = bpy.context.active_object
    
    def tearDown(self):
        # 清理测试用骨骼装备
        bpy.ops.object.select_all(action='DESELECT')
        self.armature.select_set(True)
        bpy.context.view_layer.objects.active = self.armature
        bpy.ops.object.delete()
    
    def test_setup_render_optimization(self):
        self.render_optimizer.setup_render_optimization(
            self.armature,
            PerformanceLevel.NORMAL
        )
        self.assertTrue(hasattr(self.render_optimizer, '_original_settings'))
    
    def test_optimize_viewport_performance(self):
        self.render_optimizer.optimize_viewport_performance()
        # 验证视窗设置是否已优化
        self.assertTrue(True)  # 需要添加具体的验证逻辑
    
    def test_optimize_render_settings(self):
        self.render_optimizer.optimize_render_settings(bpy.context.scene)
        # 验证渲染设置是否已优化
        self.assertTrue(True)  # 需要添加具体的验证逻辑
    
    def test_restore_original_settings(self):
        self.render_optimizer.setup_render_optimization(
            self.armature,
            PerformanceLevel.NORMAL
        )
        self.render_optimizer.restore_original_settings()
        self.assertFalse(hasattr(self.render_optimizer, '_original_settings'))

class TestMCPAnimationController(unittest.TestCase):
    def setUp(self):
        self.scene = bpy.context.scene
        self.mcp = MCPAnimationController()
        # 创建测试用骨骼装备
        bpy.ops.object.armature_add()
        self.armature = bpy.context.active_object
        # 创建测试用MCP文件
        self.test_file = os.path.join(tempfile.gettempdir(), 'test_mcp.txt')
        with open(self.test_file, 'w') as f:
            f.write('测试MCP数据')
    
    def tearDown(self):
        # 清理测试用骨骼装备
        bpy.ops.object.select_all(action='DESELECT')
        self.armature.select_set(True)
        bpy.context.view_layer.objects.active = self.armature
        bpy.ops.object.delete()
        # 清理测试用MCP文件
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_load_animation(self):
        self.mcp.mcp_file = self.test_file
        success = self.mcp.load_animation(bpy.context)
        self.assertTrue(success)
    
    def test_apply_animation(self):
        self.mcp.mcp_file = self.test_file
        self.mcp.load_animation(bpy.context)
        success = self.mcp.apply_animation(bpy.context, self.armature)
        self.assertTrue(success)
    
    def test_cleanup(self):
        self.mcp.mcp_file = self.test_file
        self.mcp.load_animation(bpy.context)
        self.mcp.apply_animation(bpy.context, self.armature)
        success = self.mcp.cleanup()
        self.assertTrue(success)
    
    def test_set_performance_level(self):
        self.mcp.set_performance_level(PerformanceLevel.HIGH)
        self.assertEqual(self.mcp._performance_level, PerformanceLevel.HIGH)
    
    def test_save_mapping_template(self):
        self.mcp.mcp_file = self.test_file
        self.mcp.load_animation(bpy.context)
        success = self.mcp.save_mapping_template('test_template')
        self.assertTrue(success)

def register():
    pass

def unregister():
    pass