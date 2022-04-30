from tkinter import *
from views.customwindow import CustomWindow

class CreditsScreen(CustomWindow):
    def __init__(self, root):
        super().__init__(root)

        # sets the title of the Toplevel widget
        self.window.title("ISTEC Typing Speed Test")
        self.window.grid_columnconfigure((0, 4), weight=1)   

        Button(self.window, text='Return', command=self.onReturn).grid(row=4, column=1, pady=10)

    def onReturn(self): 
        self.quitWindow()