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
    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(6.5, -5.12, 7.6), rotation=(0.86, 0.0, 0.89), scale=(1, 1, 1))
    scene.camera = context.object
    

    #Adding the sun
    bpy.ops.object.light_add(type='POINT', radius=10, align='WORLD', location=(-0.4, 2.58, 5.4), scale=(1, 1, 1))
    bpy.context.object.data.energy = 1000

    #Adding the plane
    bpy.ops.mesh.primitive_plane_add(size=50, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

    #Adding the object
    imported_object = bpy.ops.import_scene.obj(filepath='./geometric_model/1screw.obj')
    obj_object = bpy.context.selected_objects[0]
    bpy.context.view_layer.objects.active = obj_object
    
    #Changing the location and the size of the imported object
    
    bpy.ops.transform.resize(value=(0.134473, 0.134473, 0.134473))
    bpy.ops.transform.translate(value=(-0.2, 1.3, 0.5))
    
    #Adding the subsurface modifiers
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subdivision"].levels = 0
    bpy.ops.object.shade_smooth()
    
    #Adding Color
    #silver (0.173,0.173,0.173,1.0)
    #chrome (0.173,0.06,0.002,1.0)
    #blueish silver (0.367,0.445,0.458,1.0)




    mat = bpy.data.materials.new('PKHG')
    mat.diffuse_color = (0.367,0.445,0.458,1.0)
    mat.specular_color = (0.0,0.0,0.0)
    o = bpy.context.selected_objects[0]
    o.active_material = mat
    mat.metallic = 0.5

    #Changing render options
    #bpy.context.space_data.context = 'RENDER'
    bpy.context.scene.render.engine = 'BLENDER_EEVEE'
    bpy.context.scene.eevee.taa_samples = 1000
    bpy.context.scene.eevee.taa_render_samples = 1000
    

    #angles = [60, 90, 180]
    angles = range(0,360)
    #angles = [0, 300, 301, 302, 303, 304, 305, 306, 307]

    for angle in angles:

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects["1screw"].select_set(True)
        bpy.context.active_object.rotation_euler[2] = math.radians(angle)  

        #Render and saving the file
        
        bpy.context.scene.render.filepath = './output/000' + str(angle + 1080) + '.png'
        bpy.context.scene.render.image_settings.file_format='PNG'
        bpy.ops.render.render(use_viewport = True, write_still=True)
    


import_file()