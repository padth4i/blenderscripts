import bpy

from bpy.types import Panel

class AddMessh(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = 'Tools Tab Label'
    bl_context = 'objectmode'
    bl_category = 'category'
    
    def draw(self, context):
        self.layout.operator('mesh.primitive_cube_add', text='Add cube', icon='MESH_CUBE')
        self.layout.operator('mesh.primitive_circle_add', text='Add circle', icon='MESH_CIRCLE')
        self.layout.operator('mesh.primitive_plane_add', text='Add plane', icon='MESH_PLANE')
        self.layout.operator('mesh.primitive_uv_sphere_add', text='Add UV sphere', icon='MESH_UVSPHERE')
       self.layout.operator('mesh.primitive_ico_sphere_add', text='Add icosphere', icon='MESH_ICOSPHERE')
        self.layout.operator('mesh.primitive_cone_add', text='Add cone', icon='MESH_CONE')
        self.layout.operator('mesh.primitive_cylinder_add', text='Add cylinder', icon='MESH_CYLINDER')
        self.layout.operator('mesh.primitive_torus_add', text='Add torus', icon='MESH_TORUS')
        self.layout.operator('mesh.primitive_monkey_add', text='Add Suzanne head', icon='MESH_MONKEY')
        
def register():
    bpy.utils.register_class(AddMesh)
    
def unregister():
    bpy.utils.unregister_class(AddMesh)
    
if __name__ == '__main__':
    register()
