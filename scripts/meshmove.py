import bpy

from bpy.types import Panel

class Movement(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = 'Tools Tab Label'
    bl_context = 'object'
    bl_category = 'Move'
    
    def move(self, context):
        self.layout.operator('######', text='Translate object')

def register():
    bpy.utils.register_class(Movement)
    
def unregister():
    bpy.utils.unregister_class(Movement)
    
if __name__ == '__main__':
    register()
