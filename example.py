# This is an example plugin

def on_load(app, context):
    """Called when plugin is loaded"""
    # Example: add a menu item
    app.FileMenu.add_command(
        label="Say Hello",
        command=lambda: say_hello(app)
    )
    index = app.FileMenu.index("end")
    context.menu_items.append(index)

    # Example: keybinding
    context.track_binding(app.TextArea, "<Control-h>", lambda e: say_hello(app))


def on_unload(app, context):
    """Called when plugin is unloaded"""
    # Remove any highlights/tags/etc
    print("Plugin unloaded!")


def say_hello(app):
    from tkinter.messagebox import showinfo
    showinfo("Plugin", "Hello from plugin!")
