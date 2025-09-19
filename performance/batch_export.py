import bpy
import os
from bpy.props import StringProperty, EnumProperty, IntProperty

class BatchExport(bpy.types.PropertyGroup):
    """批量导出动画序列"""
    
    output_path: StringProperty(
        name="Output Path",
        description="Directory to save the exported frames",
        subtype='DIR_PATH'
    )
    
    file_format: EnumProperty(
        name="File Format",
        description="Output file format",
        items=[
            ('PNG', 'PNG', 'PNG image sequence'),
            ('FFMPEG', 'FFmpeg Video', 'Video file (e.g., MP4)')
        ],
        default='PNG'
    )
    
    start_frame: IntProperty(
        name="Start Frame",
        description="Start frame for export",
        default=1
    )
    
    end_frame: IntProperty(
        name="End Frame",
        description="End frame for export",
        default=250
    )

    def execute_export(self):
        """执行批量导出"""
        scene = bpy.context.scene
        
        # 保存原始设置
        original_path = scene.render.filepath
        original_format = scene.render.image_settings.file_format
        original_start = scene.frame_start
        original_end = scene.frame_end
        
        # 应用导出设置
        scene.render.filepath = self.output_path
        scene.render.image_settings.file_format = self.file_format
        scene.frame_start = self.start_frame
        scene.frame_end = self.end_frame
        
        if self.file_format == 'FFMPEG':
            scene.render.image_settings.color_mode = 'RGB'
            scene.render.ffmpeg.format = "MPEG4"
            scene.render.ffmpeg.codec = "H264"
            scene.render.ffmpeg.constant_rate_factor = 'MEDIUM'

        # 确保输出目录存在
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
            
        # 执行渲染
        bpy.ops.render.render(animation=True)
        
        # 恢复原始设置
        scene.render.filepath = original_path
        scene.render.image_settings.file_format = original_format
        scene.frame_start = original_start
        scene.frame_end = original_end
        
        print(f"Batch export completed to {self.output_path}")