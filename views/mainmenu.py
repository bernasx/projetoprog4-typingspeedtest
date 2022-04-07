from tkinter import *
from views.gamescreen import Gamescreen
from PIL import Image, ImageTk

class MainMenu:
    def __init__(self):
        #Start Tkinter GUI, set it to a resolution of 800px in width to 600px in height
        root = Tk()
        root.geometry('800x600') # TODO - maybe make this a setting?
        root.configure(bg='#d3d3d3')
        root.title("ISTEC Type Speed Test")
        def onStartTest():
            Gamescreen(root)

        def onLeaderboard():
            #show leaderboard
            pass 

        def onCredits():
            #show leaderboard
            pass 



        # position elements appropriately 
        ## give more weight to other columns to center the grid
        root.grid_columnconfigure((0, 4), weight=1)

        ## Load the image
        image=Image.open(r'logo.jpg')
        img=image.resize((256, 256))
        my_img=ImageTk.PhotoImage(img)
        imgLbl = Label(image=my_img)
        imgLbl.grid(row=0, column=1, pady=50)

        ## all the remaining elements
        Label(root, bg='#d3d3d3', text='Enter Username:').grid(row=1, column=1, padx=(0,210))
        Entry(root, width=50).grid(row=2, column=1, pady=(0,15))
        Button(root, text='Start Test', width=15, command=onStartTest).grid(row=3, column=1, pady=10)
        Button(root, text='Leaderboard', width=15, command=onLeaderboard).grid(row=4, column=1, pady=10)
        Button(root, text='Credits', width=15, command=onCredits).grid(row=5, column=1, pady=10)

        root.mainloop()