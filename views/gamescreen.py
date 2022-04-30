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
    
    currentIndex = 0
    def __init__(self, root, username):
        super().__init__(root)

        # sets the title of the Toplevel widget
        self.window.title("ISTEC Typing Speed Test")
        self.window.grid_columnconfigure((0, 4), weight=1)   

        # Text area config
        container = Frame(self.window, borderwidth=1, relief="sunken", width=600, height=350)
        container.grid_propagate(False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid(row=1, column=1, pady=10)

        self.textArea = Text(container, font=("Helvetica", 16), wrap=WORD)
        random.shuffle(WordList.wordlist)
        self.textArea.insert(INSERT,' '.join(WordList.wordlist))
        self.textArea.grid(row=0, column=0, sticky="nsew")
        self.textArea.config(state='disabled')

        for i in range(0, len(self.textArea.get("1.0",END)) + 1):
            self.textArea.tag_add(f'{i}',f'1.{i}')
        
        #textfield config
        sv = StringVar()
        sv.trace_add("write", lambda name, index,mode, sv=sv: self.onType(sv))
        self.textfield = Entry(self.window, width=50, textvariable = sv)
        self.textfield.grid(row=2, column=1, pady=(0,15))
        self.textfield.config(state= "disabled")
        self.textfield.bind("<Left>", lambda e: "break") # Disables the left arrow key
        self.textfield.bind("<Right>", lambda e: "break") # Disables the right arrow key
        self.textfield.bind("<Double-Button-1>", lambda e: "break") # Disables the mouse double click
        self.textfield.bind("<B1-Motion>", lambda e: "break")

        # rest of the elements
        self.timerLbl = Label(self.window, text='--:--',  font=("Helvetica", 24), bg='#d3d3d3')
        self.timerLbl.grid(row=0, column=1, pady=10)
        self.startButton = Button(self.window, text='Start Test', command=self.onStart)
        self.startButton.grid(row=3, column=1, pady=10)
        Button(self.window, text='Return', command=self.onReturn).grid(row=4, column=1, pady=10)

    # this is where the main logic for the game happens
    def onType(self, sv):
        self.textfield.bind("<Button-1>", lambda e: "break") # Disables the mouse button
        #if we're at 0 chars, don't do anything
        if len(sv.get()) == 0:
            self.textArea.tag_config(f"0",foreground="black")
            self.currentIndex = 0
            return
        # handle backspaces
        entrylength = len(sv.get())-1 
        if(self.currentIndex < entrylength + 1):
            self.currentIndex = entrylength + 1
            pass
        else:
            self.textArea.tag_config(f"{entrylength+1}",foreground="black")
            self.currentIndex = entrylength + 1
            return

        #color stuff correctly
        if sv.get()[-1] == self.textArea.get(f'1.{entrylength}'):
            self.textArea.tag_config(f"{entrylength}",foreground="green")
        else:
            self.textArea.tag_config(f"{entrylength}",foreground="red")

    def onReturn(self): 
        self.quitWindow()

    def onStart(self):
        self.clock() #start the countdown
        self.textfield.config(state= "normal")
        self.startButton.config(state= "disabled")

    def gameEnd(self):
        # TODO - Add DB code here to save stuff to DB if it's the end of the game
        wpm = 0
        cpm = 0
        textfieldInput = self.textfield.get()
        textareaInput = self.textArea.get('1.0', END)

        for i in range(0,len(textfieldInput.split(' '))):
            if(textfieldInput.split(' ')[i] == textareaInput.split(' ')[i]):
                wpm += 1
                cpm += len(textfieldInput.split(' ')[i])
        
        finishPopup = Toplevel(self.window)
        finishPopup.geometry('200x200')
        Label(finishPopup, text=f'Words Per Minute: {wpm}').pack()
        Label(finishPopup, text=f'Characters Per Minute: {cpm}').pack()

        self.textfield.unbind("<Button-1>") # Re-enables the mouse button
        self.textfield.delete(0, END)
        self.textfield.config(state= "disabled")
        self.startButton.config(state= "normal")
        self.timer = 60
        random.shuffle(WordList.wordlist)
        self.textArea.config(state='normal')
        self.textArea.delete('1.0', END)
        self.textArea.insert(INSERT,' '.join(WordList.wordlist))
        for tag in self.textArea.tag_names():
            self.textArea.tag_delete(tag)
        for i in range(0, len(self.textArea.get("1.0",END)) + 1):
            self.textArea.tag_add(f'{i}',f'1.{i}')
        self.textArea.config(state='disabled')
        
        

    def clock(self):
        if self.timer == 0:
            self.timerLbl.config(text=f'00:0{self.timer}')
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
        