# autosave_extension.py
import threading
import time
from tkinter.simpledialog import askinteger
from tkinter import messagebox

# Default autosave interval in seconds
DEFAULT_INTERVAL = 300

def on_load(app, context):
    # Store interval in context
    context.autosave_interval = DEFAULT_INTERVAL
    context.autosave_active = True

    # Start autosave thread
    context.autosave_thread = threading.Thread(target=lambda: autosave_loop(app, context), daemon=True)
    context.autosave_thread.start()

    # Add menu items
    app.ExtensionsMenu.add_command(label="Manage AutoSave", command=lambda: manage_autosave(app, context))
    print("[AutoSave Extension] Loaded!")

def on_unload(app, context=None):
    # Stop autosave
    if context:
        context.autosave_active = False
    print("[AutoSave Extension] Unloaded!")

def autosave_loop(app, context):
    while getattr(context, "autosave_active", True):
        interval = getattr(context, "autosave_interval", DEFAULT_INTERVAL)
        time.sleep(interval)
        if getattr(app, 'file', None) and getattr(context, "autosave_active", True):
            try:
                with open(app.file, "w", encoding="utf-8") as f:
                    f.write(app.TextArea.get("1.0", "end-1c"))
            except Exception as e:
                print(f"[AutoSave Extension] Error saving file: {e}")

def manage_autosave(app, context):
    # Ask user for new interval
    new_interval = askinteger("AutoSave Interval",
                              "Enter autosave interval in seconds:",
                              minvalue=10, maxvalue=3600,
                              initialvalue=getattr(context, "autosave_interval", DEFAULT_INTERVAL))
    if new_interval:
        context.autosave_interval = new_interval
        messagebox.showinfo("AutoSave", f"Autosave interval set to {new_interval} seconds.")
