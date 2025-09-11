# Blender Plugin Info
# This is standard metadata for the plugin.
bl_info = {
    "name": "Custom Context Menu",
    "author": "KageKirin",
    "version": (1, 2),
    "blender": (2, 80, 0),  # Minimum Blender version required
    "location": "3D Viewport > Right-Click Context Menu > CustomPlugin",
    "description": "Adds a custom menu with two operators to the 3D Viewport context menu.",
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
class CUSTOM_MT_context_menu(bpy.types.Menu):
    """The custom menu that will appear in the context menu."""

    bl_idname = "CUSTOM_MT_context_menu"
    bl_label = "CustomPlugin"

    def draw(self, context):
        """Defines the layout of the menu."""
        layout = self.layout
        # Add the 'CheckServer' operator to the menu
        layout.operator(CUSTOM_OT_check_server.bl_idname, text="Check Server Status")
        # Add the 'Fetch' operator to the menu
        layout.operator(CUSTOM_OT_fetch_data.bl_idname, text="Fetch Data")


# This function is what gets added to the main context menu.
# It adds a separator and then our custom menu.
def draw_custom_menu_in_context(self, context):
    """Draws the menu item in the 3D Viewport context menu."""
    layout = self.layout
    layout.separator()
    layout.menu(CUSTOM_MT_context_menu.bl_idname)


# A list of all classes to register/unregister
classes = (
    CUSTOM_OT_check_server,
    CUSTOM_OT_fetch_data,
    CUSTOM_MT_context_menu,
)


def register():
    """This function is called when the plugin is enabled."""
    # Register all the custom classes
    for cls in classes:
        bpy.utils.register_class(cls)

    # --- Logic to add the menu to the 3D Viewport context menu ---
    # We append our drawing function to the list of functions that draw the context menu.
    bpy.types.VIEW3D_MT_object_context_menu.append(draw_custom_menu_in_context)


def unregister():
    """This function is called when the plugin is disabled."""
    # --- Logic to remove the menu from the 3D Viewport context menu ---
    # We remove our drawing function to clean up.
    bpy.types.VIEW3D_MT_object_context_menu.remove(draw_custom_menu_in_context)

    # Unregister all the custom classes in reverse order
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


# This allows the script to be run directly in Blender's text editor
# to test the plugin without having to install it.
if __name__ == "__main__":
    register()
