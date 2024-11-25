import bpy

bpy.ops.mesh.primitive_cube_add(size=2, location=(1, 2, 3))
cube = bpy.context.object
cube.name = "TestCube"

# Print info about the cube
print(f"Created object: {cube.name} at location {cube.location}")