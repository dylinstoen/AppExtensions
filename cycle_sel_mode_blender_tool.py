import bpy

bl_info = {
    "name": "CycleSelect",
    "author": "Dylin Stoen",
    "blender": (3, 2, 5),
    "description": "Cycle through the Mesh Selection Mode (ctrl+alt+shift+u) goes left and ctrl+altshift+f) goes right",
    "category": "mesh"
}
addon_keymaps = []
class CycleSelModeRight(bpy.types.Operator):
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'EDIT'
    bl_idname = "mesh.cycle_sel_mode_right"
    bl_label = "Cycle Select Right"
    bl_description = "Cycle through the Mesh Selection Modes right"

    def execute(self, context):
        if context.active_object.mode != 'EDIT':
            return {'FINISHED'}
        options = context.tool_settings.mesh_select_mode[:]
        if options == (True, False, False):
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        if options == (False, True, False):
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        if options == (False, False, True):
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        return {'FINISHED'}

class CycleSelModeLeft(bpy.types.Operator):
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'EDIT'
    bl_idname = "mesh.cycle_sel_mode_left"
    bl_label = "Cycle Select Left"
    bl_description = "Cycle through the Mesh Selection Modes left"

    def execute(self, context):
        if context.active_object.mode != 'EDIT':
            return {'FINISHED'}
        options = context.tool_settings.mesh_select_mode[:]
        if options == (True, False, False):
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        if options == (False, True, False):
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        if options == (False, False, True):
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(CycleSelModeRight)
    bpy.utils.register_class(CycleSelModeLeft)
    addon_keymaps.clear()
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        right = km.keymap_items.new("mesh.cycle_sel_mode_right", type='U',value='PRESS', ctrl=True, alt=True, shift=True)
        left = km.keymap_items.new("mesh.cycle_sel_mode_left", type='F',value='PRESS', ctrl=True, alt=True, shift=True)
        addon_keymaps.append((km, right))
        addon_keymaps.append((km, left))
            
def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(CycleSelModeLeft)
    bpy.utils.unregister_class(CycleSelModeRight)

if __name__ == "__main__":
    register()
