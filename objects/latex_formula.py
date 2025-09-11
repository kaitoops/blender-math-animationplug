import bpy
import os
import tempfile
from bpy.props import StringProperty, FloatProperty, BoolProperty
from ..core.base import MathObjectBase

class LatexFormula(MathObjectBase):
    """LaTeX公式类，支持公式渲染和动态更新"""
    
    formula = StringProperty(
        name="Formula",
        description="LaTeX formula to render",
        default="\\sum_{n=1}^{\\infty} \\frac{1}{n^2} = \\frac{\\pi^2}{6}"
    )
    
    scale = FloatProperty(
        name="Scale",
        description="Formula scale factor",
        default=1.0,
        min=0.1
    )
    
    transparent_background = BoolProperty(
        name="Transparent Background",
        description="Use transparent background for formula",
        default=True
    )
    
    resolution = FloatProperty(
        name="Resolution",
        description="Formula render resolution in DPI",
        default=300.0,
        min=72.0
    )
    
    def create(self):
        """创建LaTeX公式对象"""
        # 检查Images as Planes插件
        if not self._check_dependencies():
            return
        
        # 创建临时LaTeX文件
        tex_content = self._generate_tex_content()
        temp_dir = tempfile.mkdtemp()
        tex_file = os.path.join(temp_dir, 'formula.tex')
        
        with open(tex_file, 'w') as f:
            f.write(tex_content)
        
        # 编译LaTeX文件
        os.system(f'pdflatex -output-directory={temp_dir} {tex_file}')
        
        # 转换PDF为PNG
        pdf_file = os.path.join(temp_dir, 'formula.pdf')
        png_file = os.path.join(temp_dir, 'formula.png')
        os.system(f'convert -density {self.resolution} {pdf_file} -quality 100 {png_file}')
        
        # 使用Images as Planes导入PNG
        bpy.ops.import_image.to_plane(
            files=[{"name": png_file}],
            directory=temp_dir,
            shader='SHADELESS',
            transparency=self.transparent_background
        )
        
        # 获取创建的对象
        self.obj = bpy.context.selected_objects[0]
        self.obj.scale = (self.scale, self.scale, self.scale)
        
        # 清理临时文件
        self._cleanup_temp_files(temp_dir)
    
    def update(self):
        """更新公式内容和属性"""
        if self.obj:
            # 重新生成公式图像
            self.delete()
            self.create()
    
    def delete(self):
        """删除公式对象"""
        if self.obj:
            # 删除材质和图像
            for mat in self.obj.data.materials:
                if mat:
                    if mat.node_tree:
                        for node in mat.node_tree.nodes:
                            if node.type == 'TEX_IMAGE' and node.image:
                                bpy.data.images.remove(node.image)
                    bpy.data.materials.remove(mat)
            
            # 删除网格数据
            mesh = self.obj.data
            bpy.data.objects.remove(self.obj, do_unlink=True)
            bpy.data.meshes.remove(mesh)
    
    def _check_dependencies(self):
        """检查必要的依赖项"""
        if not hasattr(bpy.ops, 'import_image'):
            self.report({'ERROR'}, "Images as Planes插件未启用")
            return False
        return True
    
    def _generate_tex_content(self):
        """生成LaTeX文档内容"""
        return f"\\documentclass[preview]{{standalone}}\n" \
               f"\\usepackage{{amsmath}}\n" \
               f"\\usepackage{{amssymb}}\n" \
               f"\\begin{{document}}\n" \
               f"${self.formula}$\n" \
               f"\\end{{document}}"
    
    def _cleanup_temp_files(self, temp_dir):
        """清理临时文件和目录"""
        for file in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, file))
        os.rmdir(temp_dir)