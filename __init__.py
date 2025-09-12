import bpy
from . import CustomMenu
from . import CustomContextMenu
from . import CustomNodeOperator

# This is standard metadata for the plugin.
bl_info = {
    "name": "Blender Extension Test",
    "author": "KageKirin",
    "version": (1, 0),
    "blender": (4, 5, 0),  # Minimum Blender version required
    "location": "nowhere yet",
    "description": "adds custom dialogs",
    "warning": "",
    "doc_url": "",
    "category": "Development",
}



def register():
    CustomMenu.register()
    CustomContextMenu.register()
    CustomNodeOperator.register()


def unregister():
    CustomMenu.unregister()
    CustomContextMenu.unregister()
    CustomNodeOperator.unregister()

    for pt in bpy.types.Menu.__subclasses__():
        if "bl_rna" in pt.__dict__:  # <-- check if already removed!
            bpy.utils.unregister_class(pt)
    for pt in bpy.types.Operator.__subclasses__():
        if "bl_rna" in pt.__dict__:  # <-- check if already removed!
            bpy.utils.unregister_class(pt)
    for pt in bpy.types.Panel.__subclasses__():
        if "bl_rna" in pt.__dict__:  # <-- check if already removed!
            bpy.utils.unregister_class(pt)


if __name__ == "__main__":
    register()
