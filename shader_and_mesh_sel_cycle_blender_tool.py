import bpy

bl_info = {
    "name": "Cycle Through the Mesh Selection and Shade Types",
    "author": "Dylin Stoen",
    "blender": (3, 2, 0),
    "description": "In object mode cycle the shade types but in edit mode cycle the mesh select modes",
    "category": "mesh"
}

addon_keymaps = []


class CycleMeshShadeUp(bpy.types.Operator):
    bl_idname = "mesh.cycle_mesh_shade_up"
    bl_label = "Cycle Mesh Shade Up"
    bl_description = "Cycle up, in object mode cycle the shade types but in edit mode cycle the mesh select modes"

    def execute(self, context):
        if context.active_object.mode == 'EDIT':
            SELECTMODE = context.tool_settings.mesh_select_mode[:]
            if SELECTMODE == (True, False, False):
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
            elif SELECTMODE == (False, True, False):
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            elif SELECTMODE == (False, False, True):
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        elif context.active_object.mode == 'OBJECT':
            SHADEMODE = context.space_data.shading.type
            if SHADEMODE == 'WIREFRAME':
                bpy.context.space_data.shading.type = 'SOLID'
            elif SHADEMODE == 'SOLID':
             bpy.context.space_data.shading.type = 'MATERIAL'
            elif SHADEMODE == 'MATERIAL':
                bpy.context.space_data.shading.type = 'RENDERED'
            elif SHADEMODE == 'RENDERED':
                bpy.context.space_data.shading.type = 'WIREFRAME'
        return {'FINISHED'}

class CycleMeshShadeDown(bpy.types.Operator):
    bl_idname = "mesh.cycle_mesh_shade_down"
    bl_label = "Cycle Mesh Shade Down"
    bl_description = "Cycle down, in object mode cycle the shade types but in edit mode cycle the mesh select modes

    def execute(self, context):
        if context.active_object.mode == 'EDIT':
            SELECTMODE = context.tool_settings.mesh_select_mode[:]
            if SELECTMODE == (True, False, False):
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            elif SELECTMODE == (False, True, False):
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            elif SELECTMODE == (False, False, True):
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        elif context.active_object.mode == 'OBJECT':
            SHADEMODE = context.space_data.shading.type
            if SHADEMODE == 'WIREFRAME':
                bpy.context.space_data.shading.type = 'RENDERED'
            elif SHADEMODE == 'RENDERED':
                bpy.context.space_data.shading.type = 'MATERIAL'
            elif SHADEMODE == 'MATERIAL':
                bpy.context.space_data.shading.type = 'SOLID'
            elif SHADEMODE == 'SOLID':
                bpy.context.space_data.shading.type = 'WIREFRAME'
        return {'FINISHED'}

def register():
    bpy.utils.register_class(CycleMeshShadeUp)
    bpy.utils.register_class(CycleMeshShadeDown)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    key_assign_list = [
        (CycleMeshShadeUp.bl_idname, "M", "PRESS", True, True, False),
        (CycleMeshShadeDown.bl_idname, "N", "PRESS", True, True, False)
        ]
    if kc:
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        for (idname, key, event, ctrl, alt, shift) in key_assign_list:
            kmi = km.keymap_items.new(
                idname, key, event, ctrl=ctrl, alt=alt, shift=shift)
            addon_keymaps.append((km, kmi))


def unregister():
    bpy.utils.register_class(CycleMeshShadeUp)
    bpy.utils.register_class(CycleMeshShadeDown)
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
