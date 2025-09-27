import customtkinter as tk
from stylesheet import *

def profile_creator(screen = None):
    login = EntryBox(screen, placeholder_text = "Username")
    login.grid(row = 0, column = 0)
