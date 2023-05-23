import bpy
import math
import mathutils
import numpy
bl_info = {
    "name": "View Parents XRay Rebinder",
    "author": "Dylin Stoen",
    "blender": (3, 2, 0),
    "description": "Alternate between binding two different Blender modes iff the binding of the parent feature has been satisified",
    "category": "mesh"
}

addon_keymaps = []
class RebindViewToXRay(bpy.types.Operator):
    bl_idname = "mesh.view_xray_rebinder"
    bl_label = "Rebinder"
    bl_description = "Ortho 'Back' parents Toogle XRay mode"

    def execute(self, context):
        if context.region_data.is_orthographic_side_view:
            ROT = [math.floor(math.degrees(i)) for i in mathutils.Quaternion.to_euler(context.region_data.view_rotation)[:]]
            if ROT == [90.0, 0.0, 180.0]:
                bpy.ops.view3d.toggle_xray()
            else:
                bpy.ops.view3d.view_axis(type='BACK')
        else:
            bpy.ops.view3d.view_axis(type='BACK')
        return {'FINISHED'}


def register():
    bpy.utils.register_class(RebindViewToXRay)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    key_assign_list = [
        (RebindViewToXRay.bl_idname, "E", "PRESS", True, True, False)
        ]
    if kc:
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        for (idname, key, event, ctrl, alt, shift) in key_assign_list:
            kmi = km.keymap_items.new(
                idname, key, event, ctrl=ctrl, alt=alt, shift=shift)
            addon_keymaps.append((km, kmi))


def unregister():
    bpy.utils.register_class(RebindViewToXRay)
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
