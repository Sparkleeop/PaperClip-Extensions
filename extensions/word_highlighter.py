# highlight_word_extension.py

def on_load(app, context):
    # Add menu item and track its index
    app.FileMenu.add_command(
        label="Highlight Word...",
        command=lambda: highlight_word(app)
    )
    index = app.FileMenu.index("end")
    context.menu_items.append(index)

    # Example keybinding tracked
    context.track_binding(app.TextArea, "<Control-h>", lambda e: highlight_word(app))

    print("[Highlight Extension] Loaded!")

def on_unload(app, context):
    # Remove highlight tags
    app.TextArea.tag_delete("highlight")
    print("[Highlight Extension] Unloaded!")

def highlight_word(app):
    from tkinter.simpledialog import askstring

    word = askstring("Highlight", "Enter a word to highlight:")
    if not word:
        return

    app.TextArea.tag_delete("highlight")
    app.TextArea.tag_config("highlight", background="yellow", foreground="black")

    start = "1.0"
    while True:
        start = app.TextArea.search(word, start, stopindex="end")
        if not start:
            break
        end = f"{start}+{len(word)}c"
        app.TextArea.tag_add("highlight", start, end)
        start = end
