# darker_mode_extension.py

def on_load(app, context):
    context.menu_items.append(
        app.FileMenu.add_command(
            label="Toggle Darker Mode",
            command=lambda: toggle_darker_mode(app)
        )
    )
    print("[Darker Mode Extension] Loaded!")

def on_unload(app, context=None):
    # Resetting is optional
    print("[Darker Mode Extension] Unloaded!")

def toggle_darker_mode(app):
    current_bg = app.TextArea.cget("bg")
    if current_bg == "#1e1e1e":
        app.TextArea.config(bg="#121212", fg="#e0e0e0")
    else:
        app.TextArea.config(bg="#1e1e1e", fg="#d4d4d4")
