import bpy
from . import CustomMenu

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


def unregister():
    CustomMenu.unregister()


if __name__ == "__main__":
    register()
