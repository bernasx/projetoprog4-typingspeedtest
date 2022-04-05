#code for the game goes here, as a separate window
from tkinter import *

class Gamescreen:
    def __init__(self, root):
        # Toplevel object which will be treated as a new window
        window = Toplevel(root)

        # save the class attributes to close the window afterwards
        self.root = root
        self.window = window
        root.withdraw()
        
        # sets the title of the Toplevel widget
        window.title("Game")
        # sets the geometry of toplevel
        window.geometry("800x600")

        # TODO - Use a grid instead of packing these
        Label(window,text ="This is a new window").pack() 
        Button(window, text='Return', command=self.onReturn).pack()

    def onReturn(self):
        self.root.deiconify()
        # TODO - Add DB code here to save stuff to DB if it's the end of the game
        self.window.destroy()