import bpy

bl_info = {
    "name": "Cycle Through Shading Types",
    "author": "Dylin Stoen",
    "blender": (3, 2, 0),
    "description": "Cycle between all of the Shading Types. Default keybindings: Ctrl+Alt+O cycles up and Ctrl+Alt+K cycles down",
    "category": "mesh"
}

addon_keymaps = []


class CycleShadingTypeUp(bpy.types.Operator):
    bl_idname = "mesh.cycle_shade_type_up"
    bl_label = "Cycle Shade Type Up"
    bl_description = "Cycle up through the different mesh selection modes using a single hotkey (Wireframe->Solid->Material->Rendered)."

    def execute(self, context):
        SHADEMODE = context.space_data.shading.type
        if SHADEMODE == 'WIREFRAME':
            bpy.context.space_data.shading.type = 'SOLID'
        if SHADEMODE == 'SOLID':
            bpy.context.space_data.shading.type = 'MATERIAL'
        if SHADEMODE == 'MATERIAL':
            bpy.context.space_data.shading.type = 'RENDERED'
        if SHADEMODE == 'RENDERED':
            bpy.context.space_data.shading.type = 'WIREFRAME'

        return {'FINISHED'}

class CycleShadingTypeDown(bpy.types.Operator):
    bl_idname = "mesh.cycle_shade_type_down"
    bl_label = "Cycle Shade Type Down"
    bl_description = "Cycle down through the different mesh selection modes using a single hotkey (Wireframe->Rendered->Material->Solid)."

    def execute(self, context):
        SHADEMODE = context.space_data.shading.type
        if SHADEMODE == 'WIREFRAME':
            bpy.context.space_data.shading.type = 'RENDERED'
        if SHADEMODE == 'RENDERED':
            bpy.context.space_data.shading.type = 'MATERIAL'
        if SHADEMODE == 'MATERIAL':
            bpy.context.space_data.shading.type = 'SOLID'
        if SHADEMODE == 'SOLID':
            bpy.context.space_data.shading.type = 'WIREFRAME'


        return {'FINISHED'}

def register():
    bpy.utils.register_class(CycleShadingTypeUp)
    bpy.utils.register_class(CycleShadingTypeDown)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    key_assign_list = [
        (CycleShadingTypeUp.bl_idname, "O", "PRESS", True, True, False),
        (CycleShadingTypeDown.bl_idname, "K", "PRESS", True, True, False)
        ]
    if kc:
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        for (idname, key, event, ctrl, alt, shift) in key_assign_list:
            kmi = km.keymap_items.new(
                idname, key, event, ctrl=ctrl, alt=alt, shift=shift)
            addon_keymaps.append((km, kmi))


def unregister():
    bpy.utils.register_class(CycleShadingTypeUp)
    bpy.utils.register_class(CycleShadingTypeDown)
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
