# syntax_highlight_extension.py
KEYWORDS = ["def", "class", "import", "for", "while", "if", "else", "elif", "return"]

def on_load(app, context):
    app.TextArea.bind("<KeyRelease>", lambda e: highlight(app))
    print("[Syntax Highlight Extension] Loaded!")

def on_unload(app, context=None):
    app.TextArea.tag_delete("keyword")
    print("[Syntax Highlight Extension] Unloaded!")

def highlight(app):
    text = app.TextArea.get("1.0", "end-1c")
    app.TextArea.tag_delete("keyword")
    app.TextArea.tag_config("keyword", foreground="orange")
    for word in KEYWORDS:
        start = "1.0"
        while True:
            start = app.TextArea.search(r"\b" + word + r"\b", start, stopindex="end", regexp=True)
            if not start:
                break
            end = f"{start}+{len(word)}c"
            app.TextArea.tag_add("keyword", start, end)
            start = end
