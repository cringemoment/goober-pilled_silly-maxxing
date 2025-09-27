import customtkinter as tk
from stylesheet import *

from signup import signup_screen

def login_screen(s = None):
    clear(s)
    usernamebox = EntryBox(s, placeholder_text = "Username", width = 300, height = 50, justify = "center")
    usernamebox.grid(row = 0)

    password = EntryBox(s, placeholder_text = "Password", width = 300, height = 50, justify = "center")
    password.grid(row = 1)

    createaccount = Hyperlink(signup_screen, master = s, text = "asda")
    createaccount.grid(row = 2)
