#code for the test goes here
from tkinter import *
import random 
from views.customwindow import CustomWindow
from utils.wordlist import WordList

class Gamescreen(CustomWindow):
    ingame = False
    textfield = 0
    textArea = 0
    timerLbl = 0
    startButton = 0
    timer = 60

    def __init__(self, root):
        super().__init__(root)

        # sets the title of the Toplevel widget
        self.window.title("ISTEC Typing Speed Test")
        self.window.grid_columnconfigure((0, 4), weight=1)   

        # Text area config
        container = Frame(self.window, borderwidth=1, relief="sunken", width=600, height=250)
        container.grid_propagate(False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid(row=1, column=1, pady=10)

        self.textArea = Text(container, font=("Helvetica", 16), wrap=WORD)
        random.shuffle(WordList.wordlist)
        self.textArea.insert(INSERT,' '.join(WordList.wordlist))
        self.textArea.grid(row=0, column=0, sticky="nsew")
        self.textArea.config(state='disabled')
        
        #textfield config
        self.textfield = Entry(self.window, width=50)
        self.textfield.grid(row=2, column=1, pady=(0,15))
        self.textfield.config(state= "disabled")

        # rest of the elements
        self.timerLbl = Label(self.window, text='--:--')
        self.timerLbl.grid(row=0, column=1, pady=10)
        self.startButton = Button(self.window, text='Start Test', command=self.onStart)
        self.startButton.grid(row=3, column=1, pady=10)
        Button(self.window, text='Return', command=self.onReturn).grid(row=4, column=1, pady=10)

    def onReturn(self): 
        self.quitWindow()

    def onStart(self):
        self.clock() #start the countdown
        self.textfield.config(state= "normal")
        self.startButton.config(state= "disabled")

    def gameEnd(self):
        # TODO - Add DB code here to save stuff to DB if it's the end of the game
        self.textfield.config(state= "disabled")
        self.startButton.config(state= "normal")
        self.timer = 60

    def clock(self):
        if self.timer == 0:
            self.timerLbl.config(text=f'00:{self.timer}')
            self.gameEnd()
            return
        if self.timer == 60:
            self.timerLbl.config(text='01:00')
            self.timer -= 1
        else:
            # properly represent the correct amount of digits for the countdown
            if self.timer >= 10:
                self.timerLbl.config(text=f'00:{self.timer}')
            else:
                self.timerLbl.config(text=f'00:0{self.timer}')
            self.timer -= 1
        self.timerLbl.after(1000, self.clock)
        