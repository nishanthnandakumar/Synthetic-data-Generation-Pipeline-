import bpy
import math
from bpy import context
from math import radians


#### The following code is used for cleaning the scene ####
def purge_orphans():
    if bpy.app.version >= (3, 0, 0):
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True, do_linked_ids=True, do_recursive=True
        )
    else:
        # call purge_orphans() recursively until there are no more orphan data blocks to purge
        result = bpy.ops.outliner.orphans_purge()
        if result.pop() != "CANCELLED":
            purge_orphans()

def clean_scene():
    """
    Removing all of the objects, collection, materials, particles,
    textures, images, curves, meshes, actions, nodes, and worlds from the scene
    """
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
        bpy.ops.object.editmode_toggle()

    for obj in bpy.data.objects:
        obj.hide_set(False)
        obj.hide_select = False
        obj.hide_viewport = False

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

    collection_names = [col.name for col in bpy.data.collections]
    for name in collection_names:
        bpy.data.collections.remove(bpy.data.collections[name])

    # in the case when you modify the world shader
    world_names = [world.name for world in bpy.data.worlds]
    for name in world_names:
        bpy.data.worlds.remove(bpy.data.worlds[name])
    # create a new world data block
    bpy.ops.world.new()
    bpy.context.scene.world = bpy.data.worlds["World"]
    
    purge_orphans()
    
def import_file():
    
    clean_scene()
    scene = context.scene

    #Adding a camera

    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(6.5, 0, 1.5), rotation=(1.41649, 0, 1.59684), scale=(1, 1, 1))
    scene.camera = context.object
    

    #Adding the sun
    bpy.ops.object.light_add(type='POINT', radius=0.1, align='WORLD', location=(7, 0.0, 5.0), scale=(1, 1, 1))
    bpy.context.object.data.energy = 1000

    #Adding the cylinder
    imported_object = bpy.ops.import_mesh.stl(filepath='/root/src/geometric_model/cylinder_new.STL')
    obj_object = bpy.context.selected_objects[0]
    obj_object.name = "cylinder_new"
    
    #object transformation
    obj_object.location = (-1.0, 1.0, 0.0)  # X, Y, Z in Blender units
    obj_object.scale = (0.05, 0.05, 0.05)     # Uniform scaling
    obj_object.rotation_euler = (
        radians(90),  # X rotation
        radians(0),   # Y rotation
        radians(0)   # Z rotation
    )

    bpy.context.view_layer.objects.active = obj_object              
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')

    # Create a new material
    material = bpy.data.materials.new(name="CustomMaterial")
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = (0.800047, 0.0520891, 0.00980674, 1)  # RGBA, values between 0 and 1
        bsdf.inputs['Roughness'].default_value = 0.698413

    # Assign material to the imported object
    if obj_object.data.materials:
        obj_object.data.materials[0] = material
    else:
        obj_object.data.materials.append(material)


    #Add temp_sensor.stl

    bpy.ops.import_mesh.stl(filepath='/root/src/geometric_model/temp_sensor.STL')
    sensor_object = bpy.context.selected_objects[0]
    sensor_object.name = "temp_sensor"

    sensor_object.location = (-1.0, 0.99, 0.86)
    sensor_object.scale = (0.05, 0.05, 0.05)
    sensor_object.rotation_euler = (radians(90), radians(0), radians(0))

    bpy.context.view_layer.objects.active = sensor_object           
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')

    sensor_material = bpy.data.materials.new(name="SensorMaterial")
    sensor_material.use_nodes = True
    bsdf2 = sensor_material.node_tree.nodes.get("Principled BSDF")
    if bsdf2:
        bsdf2.inputs['Base Color'].default_value = (0.451586, 0.427353, 0.3903, 1)
        bsdf2.inputs['Roughness'].default_value = 0.389637
        bsdf2.inputs['Metallic'].default_value = 0.569215

    if sensor_object.data.materials:
        sensor_object.data.materials[0] = sensor_material
    else:
        sensor_object.data.materials.append(sensor_material)
    

    #Changing render options

    bpy.context.scene.render.engine = 'BLENDER_EEVEE'
    bpy.context.scene.eevee.taa_samples = 1000
    bpy.context.scene.eevee.taa_render_samples = 1000

    #Resolution
    bpy.context.scene.render.resolution_x = 1024
    bpy.context.scene.render.resolution_y = 1024

    cylinder = bpy.data.objects["cylinder_new"]           
    sensor = bpy.data.objects["temp_sensor"]              

    angles = range(0, 360, 15)                            

    for angle in angles:
        rad = math.radians(angle)                          
        cylinder.rotation_euler.z = rad                    
        sensor.rotation_euler.z = rad                      

        bpy.context.scene.render.filepath = f'/root/src/output/model1/rot_{angle:03d}.png'  
        bpy.context.scene.render.image_settings.file_format = 'JPEG'
        bpy.ops.render.render(write_still=True)
    

import_file()