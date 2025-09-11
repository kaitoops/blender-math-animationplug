import bpy
from bpy.props import EnumProperty, StringProperty

class MaterialSystem(bpy.types.PropertyGroup):
    """材质系统，提供预设节点组"""
    
    preset = EnumProperty(
        name="Preset",
        description="Select a material preset",
        items=[
            ('DEFAULT', 'Default', 'Default PBR material'),
            ('CARTOON', 'Cartoon', 'Cartoon/Toon shader'),
            ('TRANSLUCENT', 'Translucent', 'Translucent material'),
            ('METALLIC', 'Metallic', 'Metallic material')
        ],
        default='DEFAULT'
    )
    
    node_group_name = StringProperty(
        name="Node Group Name",
        description="Name of the generated node group",
        default="MathMaterialPreset"
    )
    
    def apply(self, target_object):
        """应用材质预设到对象"""
        if not target_object or not target_object.data.materials:
            # 如果没有材质，则创建一个
            mat = bpy.data.materials.new(name="MathMaterial")
            mat.use_nodes = True
            target_object.data.materials.append(mat)
        else:
            mat = target_object.data.materials[0]
            
        # 创建或获取节点组
        node_group = self._get_or_create_node_group()
        
        # 在材质中添加节点组实例
        nodes = mat.node_tree.nodes
        group_node = nodes.new('ShaderNodeGroup')
        group_node.node_tree = node_group
        
        # 连接到输出
        output_node = nodes.get('Material Output')
        if output_node:
            mat.node_tree.links.new(group_node.outputs[0], output_node.inputs[0])

    def _get_or_create_node_group(self):
        """获取或创建预设节点组"""
        if self.node_group_name in bpy.data.node_groups:
            return bpy.data.node_groups[self.node_group_name]
        
        # 创建新节点组
        node_group = bpy.data.node_groups.new(self.node_group_name, 'ShaderNodeTree')
        
        # 添加输入输出
        group_inputs = node_group.nodes.new('NodeGroupInput')
        group_outputs = node_group.nodes.new('NodeGroupOutput')
        
        node_group.inputs.new('NodeSocketColor', 'Base Color')
        node_group.outputs.new('NodeSocketShader', 'Shader')
        
        # 根据预设创建节点
        if self.preset == 'DEFAULT':
            self._create_default_preset(node_group, group_inputs, group_outputs)
        elif self.preset == 'CARTOON':
            self._create_cartoon_preset(node_group, group_inputs, group_outputs)
        elif self.preset == 'TRANSLUCENT':
            self._create_translucent_preset(node_group, group_inputs, group_outputs)
        elif self.preset == 'METALLIC':
            self._create_metallic_preset(node_group, group_inputs, group_outputs)
            
        return node_group

    def _create_default_preset(self, group, inputs, outputs):
        """创建默认PBR预设"""
        principled = group.nodes.new('ShaderNodeBsdfPrincipled')
        group.links.new(inputs.outputs[0], principled.inputs['Base Color'])
        group.links.new(principled.outputs[0], outputs.inputs[0])

    def _create_cartoon_preset(self, group, inputs, outputs):
        """创建卡通着色器预设"""
        shader_to_rgb = group.nodes.new('ShaderNodeShaderToRGB')
        color_ramp = group.nodes.new('ShaderNodeValToRGB')
        diffuse = group.nodes.new('ShaderNodeBsdfDiffuse')
        
        color_ramp.color_ramp.elements.new(0.5)
        color_ramp.color_ramp.elements[0].color = (0.2, 0.2, 0.2, 1)
        color_ramp.color_ramp.elements[1].color = (0.8, 0.8, 0.8, 1)
        
        group.links.new(inputs.outputs[0], diffuse.inputs['Color'])
        group.links.new(diffuse.outputs[0], shader_to_rgb.inputs[0])
        group.links.new(shader_to_rgb.outputs[0], color_ramp.inputs[0])
        group.links.new(color_ramp.outputs[0], outputs.inputs[0])

    def _create_translucent_preset(self, group, inputs, outputs):
        """创建半透明材质预设"""
        translucent = group.nodes.new('ShaderNodeBsdfTranslucent')
        group.links.new(inputs.outputs[0], translucent.inputs['Color'])
        group.links.new(translucent.outputs[0], outputs.inputs[0])

    def _create_metallic_preset(self, group, inputs, outputs):
        """创建金属材质预设"""
        principled = group.nodes.new('ShaderNodeBsdfPrincipled')
        principled.inputs['Metallic'].default_value = 1.0
        principled.inputs['Roughness'].default_value = 0.2
        
        group.links.new(inputs.outputs[0], principled.inputs['Base Color'])
        group.links.new(principled.outputs[0], outputs.inputs[0])