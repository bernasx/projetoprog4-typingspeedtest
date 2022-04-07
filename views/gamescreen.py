#code for the test goes here
from tkinter import *
import random 
from views.customwindow import CustomWindow
from utils.wordlist import WordList

class Gamescreen(CustomWindow):
    ingame = False

    def __init__(self, root):
        super().__init__(root)

        # sets the title of the Toplevel widget
        self.window.title("Game")
        self.window.grid_columnconfigure((0, 4), weight=1)   

        # Text area config
        textArea = Text(self.window)
        random.shuffle(WordList.wordlist)
        textArea.insert(INSERT,' '.join(WordList.wordlist))
        textArea.grid(row=0, column=1, pady=10)

        # rest of the elements
        
        textfield = Entry(self.window, width=50)
        textfield.grid(row=1, column=1, pady=(0,15))
        textfield.config(state= "disabled")
        Button(self.window, text='Start Test', command=self.onStart).grid(row=2, column=1, pady=10)
        Button(self.window, text='Return', command=self.onReturn).grid(row=3, column=1, pady=10)
        

    def onReturn(self): 
        # TODO - Add DB code here to save stuff to DB if it's the end of the game
        self.quitWindow()

    def onStart(self):
        pass