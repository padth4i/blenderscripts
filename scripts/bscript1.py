import bpy

for ob in bpy.context.scene.objects:
    print(ob.name)
    
bpy.ops.mesh.primitive_monkey_add()

bpy.ops.transform.rotate(axis=(0,45,45))

bpy.ops.transform.translate(value=(0,2,0))
