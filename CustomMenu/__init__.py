# Blender Plugin Info
# This is standard metadata for the plugin.
bl_info = {
    "name": "Custom Topbar Menu",
    "author": "KageKirin",
    "version": (1, 0),
    "blender": (2, 80, 0),  # Minimum Blender version required
    "location": "Topbar > CustomPlugin",
    "description": "Adds a custom menu with two operators to the topbar.",
    "warning": "",
    "doc_url": "",
    "category": "Development",
}

import bpy


# Define the first operator: CheckServer
class CUSTOM_OT_check_server(bpy.types.Operator):
    """Checks the status of a hypothetical server."""

    bl_idname = "custom.check_server"  # Unique identifier for the operator
    bl_label = "Check Server"  # Text that appears on the button

    def execute(self, context):
        """This method is called when the operator is executed."""
        print("Checking server status... Server is OK!")
        # You can show a message in the Blender UI as well
        self.report({"INFO"}, "Server check complete. Status: OK!")
        return {"FINISHED"}  # Indicates the operator finished successfully


# Define the second operator: Fetch
class CUSTOM_OT_fetch_data(bpy.types.Operator):
    """Fetches data from a hypothetical source."""

    bl_idname = "custom.fetch_data"  # Unique identifier for the operator
    bl_label = "Fetch"  # Text that appears on the button

    def execute(self, context):
        """This method is called when the operator is executed."""
        print("Fetching data from the server...")
        self.report({"INFO"}, "Fetching data...")
        return {"FINISHED"}  # Indicates the operator finished successfully


# Define the menu that will hold the operators
class TOPBAR_MT_custom_menu(bpy.types.Menu):
    """The custom menu that will appear in the topbar."""

    bl_idname = "TOPBAR_MT_custom_menu"
    bl_label = "CustomPlugin"

    def draw(self, context):
        """Defines the layout of the menu."""
        layout = self.layout
        # Add the 'CheckServer' operator to the menu
        layout.operator(CUSTOM_OT_check_server.bl_idname, text="Check Server Status")
        # Add the 'Fetch' operator to the menu
        layout.operator(CUSTOM_OT_fetch_data.bl_idname, text="Fetch Data")


# A function to draw the menu in the topbar
def draw_custom_menu(self, context):
    """Draws the menu label in the topbar."""
    self.layout.menu(TOPBAR_MT_custom_menu.bl_idname)


# A list of all classes to register/unregister
classes = (
    CUSTOM_OT_check_server,
    CUSTOM_OT_fetch_data,
    TOPBAR_MT_custom_menu,
)


def register():
    """This function is called when the plugin is enabled."""
    # Register all the custom classes
    for cls in classes:
        bpy.utils.register_class(cls)
    # Add the draw function to the topbar's main menu area
    bpy.types.TOPBAR_MT_editor_menus.append(draw_custom_menu)


def unregister():
    """This function is called when the plugin is disabled."""
    # Remove the draw function from the topbar
    bpy.types.TOPBAR_MT_editor_menus.remove(draw_custom_menu)
    # Unregister all the custom classes in reverse order
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


# This allows the script to be run directly in Blender's text editor
# to test the plugin without having to install it.
if __name__ == "__main__":
    register()
