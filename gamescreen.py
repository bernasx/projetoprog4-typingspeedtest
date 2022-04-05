#code for the game goes here, as a separate window
from tkinter import *

def start(root):
    # Toplevel object which will    
    # be treated as a new window
    window = Toplevel(root)
    # sets the title of the Toplevel widget
    window.title("Game")
 
    # sets the geometry of toplevel
    window.geometry("800x600")
 
    # A Label widget to show in toplevel
    Label(window, text ="This is a new window").pack() 