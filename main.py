from tkinter import *
import gamescreen
from PIL import Image, ImageTk

#Start Tkinter GUI, set it to a resolution of 800px in width to 600px in height
root = Tk()
root.geometry('800x600')
root.configure(bg='#d3d3d3')

def onStartTest():
    gamescreen.start(root)
    pass

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
image=Image.open('logo.jpg')
img=image.resize((256, 256))
my_img=ImageTk.PhotoImage(img)
imgLbl = Label(image=my_img)
imgLbl.grid(row=0, column=1, pady=50)

## all the elements
usernameLbl = Label(root, bg='#d3d3d3', text='Enter Username:')
usernameLbl.grid(row=1, column=1, padx=(0,210))

usernameEntry = Entry(root, width=50)
usernameEntry.grid(row=2, column=1, pady=(0,15))

mainBtn = Button(root, text='Start Test', width=15, command=onStartTest)
mainBtn.grid(row=3, column=1, pady=10)

leaderboardBtn = Button(root, text='Leaderboard', width=15, command=onLeaderboard)
leaderboardBtn.grid(row=4, column=1, pady=10)

creditsBtn = Button(root, text='Credits', width=15, command=onCredits)
creditsBtn.grid(row=5, column=1, pady=10)

root.mainloop()