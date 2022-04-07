# base class for all windows that will open in the menu
from tkinter import *
class CustomWindow:
     def __init__(self, root):
        # Toplevel object which will be treated as a new window
        window = Toplevel(root)
        # save the class attributes and position info to close the window afterwards
        self.root = root
        self.window = window
        root_x = root.winfo_rootx()
        root_y = root.winfo_rooty()
        window.geometry(f'+{root_x}+{root_y}')
        window.geometry('800x600')
        root.withdraw()

     def quitWindow(self):
         self.root.deiconify()
         self.window.destroy()