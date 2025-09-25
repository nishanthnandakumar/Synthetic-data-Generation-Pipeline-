import bpy
import math
from bpy import context


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

    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(-0.66986, -0.5189, 16), rotation=(-0.00825, 0, 1.49695), scale=(1, 1, 1))
    scene.camera = context.object
    

    #Adding the sun
    bpy.ops.object.light_add(type='POINT', radius=10, align='WORLD', location=(0.0, 0.0, 15.0), scale=(1, 1, 1))
    bpy.context.object.data.energy = 1000

    #Adding the plane
    bpy.ops.mesh.primitive_plane_add(size=50, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    mat = bpy.data.materials.new('PKHG')
    mat.diffuse_color = (1.0, 0.966967, 0.0384168, 1.0)
    mat.specular_color = (0.0,0.0,0.0)
    o = bpy.context.selected_objects[0]
    o.active_material = mat
    mat.metallic = 0.0

    #Adding the object
    imported_object = bpy.ops.import_mesh.stl(filepath='/root/src/geometric_model/model.STL')
    obj_object = bpy.context.selected_objects[0]
    bpy.context.view_layer.objects.active = obj_object
    
    #Changing the location and the size of the imported object
    
    bpy.ops.transform.resize(value=(0.07737, 0.07737, 0.07737))
    bpy.context.object.rotation_euler[0] = 1.5708
    #bpy.ops.transform.translate(value=(-1.167, -1.489, 0.0))

    mat = bpy.data.materials.new('PKHG')
    mat.diffuse_color = (0.0293208, 0.517565,0.578364,1.0)
    mat.specular_color = (0.0,0.0,0.0)
    o = bpy.context.selected_objects[0]
    o.active_material = mat
    mat.metallic = 0.5

    #Changing render options

    bpy.context.scene.render.engine = 'BLENDER_EEVEE'
    bpy.context.scene.eevee.taa_samples = 1000
    bpy.context.scene.eevee.taa_render_samples = 1000

    #Resolution
    bpy.context.scene.render.resolution_x = 1024
    bpy.context.scene.render.resolution_y = 1024

    angles = range(0,360, 15)

    for angle in angles:

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects["model"].select_set(True)
        bpy.context.active_object.rotation_euler[2] = math.radians(angle)  

        #Render and saving the file
        
        bpy.context.scene.render.filepath = '/root/src/output/model1/000' + str(angle) + '.png'
        bpy.context.scene.render.image_settings.file_format='JPEG'
        bpy.ops.render.render(use_viewport = True, write_still=True)
    


import_file()