from tkinter import *
from views.customwindow import CustomWindow
import webbrowser


class CreditsScreen(CustomWindow):
    def __init__(self, root):
        super().__init__(root)

        # sets the title of the Toplevel widget
        self.window.title("ISTEC Typing Speed Test")
        self.window.grid_columnconfigure((0, 4), weight=1)  
        
        imgLbl = Label(self.window, image='logo', background='#d3d3d3')
        imgLbl.grid(row=0, column=1, pady=10)
    

        Label(self.window, bg='#d3d3d3', text='Bernardo Ribeiro nrº50021\n\nTatiana Martins nrº50031\n\nPedro Gonçalves nº50032', font=("Helvetica", 12)).grid(row=6, column=1)
        gitHubLink = Label(self.window, text = "https://github.com/bernasx/projetoprog4-typingspeedtest", font=('Helveticabold 12 underline'), bg='#d3d3d3', fg="blue")
        gitHubLink.grid(row=7, column=1, pady=5)
        gitHubLink.bind("<Button-1>", lambda e: self.openUrl("https://github.com/bernasx/projetoprog4-typingspeedtest"))
        Button(self.window, text='Return', command=self.onReturn).grid(row=8, column=1, pady=(150,0))

    def onReturn(self): 
        self.quitWindow()

    def openUrl(self,url):
        webbrowser.open_new(url)