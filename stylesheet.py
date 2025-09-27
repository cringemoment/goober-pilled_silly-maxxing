import customtkinter as tk

def clear(screen):
    for widget in screen.winfo_children():
        widget.destroy()

class EntryBox(tk.CTkEntry):
    pass

class Text(tk.CTkLabel):
    def __init(self, *args, **kwargs):
        super().__init__(**kwargs)

class Hyperlink(tk.CTkLabel):
    def __init__(self, link = None, *args, **kwargs):
        super().__init__(**kwargs, text_color = "#1de1e9")
        self.bind("<Button-1>", lambda _: link(self.master))
