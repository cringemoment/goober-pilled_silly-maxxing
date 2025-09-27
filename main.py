import customtkinter as tk

from login import login_screen

s = tk.CTk()
s.geometry("800x600")

login_screen(s)

s.mainloop()
