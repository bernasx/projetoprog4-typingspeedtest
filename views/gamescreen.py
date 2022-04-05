#code for the test goes here
from tkinter import *
from views.customwindow import CustomWindow

class Gamescreen(CustomWindow):
    def __init__(self, root):
        super().__init__(root)

        # sets the title of the Toplevel widget
        self.window.title("Game")
        # TODO - Use a grid instead of packing these
        Label(self.window,text ="This is a new window").pack() 
        Button(self.window, text='Return', command=self.onReturn).pack()

    def onReturn(self):
        # TODO - Add DB code here to save stuff to DB if it's the end of the game
        self.quitWindow()