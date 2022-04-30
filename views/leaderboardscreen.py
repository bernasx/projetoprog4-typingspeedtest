from tkinter import *
from tkinter.ttk import Treeview
from views.customwindow import CustomWindow
from utils.database import Database
class LeaderboardScreen(CustomWindow):
    def __init__(self, root):
        super().__init__(root)

        # sets the title of the Toplevel widget
        self.window.title("ISTEC Typing Speed Test")
        self.window.grid_columnconfigure((0, 4), weight=1)   
        
        # setup table
        table = Treeview(self.window, columns=('date','player','wpm','cpm'))
        table.column("#0", width=0,  stretch=NO)
        table.column("date",anchor=CENTER, width=150)  
        table.column("player",anchor=CENTER, width=150)  
        table.column("wpm",anchor=CENTER, width=80)  
        table.column("cpm",anchor=CENTER, width=80)   
        table.heading("#0",text="",anchor=CENTER)
        table.heading("date",text="Date",anchor=CENTER)
        table.heading("player",text="Player",anchor=CENTER)
        table.heading("wpm",text="WPM",anchor=CENTER)
        table.heading("cpm",text="CPM",anchor=CENTER)
        table.grid(row=3, column=1, pady=10)
        
        #database stuff
        db = Database()
        data = db.fetchAllQuery('''SELECT * FROM games''')
        count = 0
        for game in data:
            table.insert(parent='',index='end',text='', iid=count, values=game)
            count+=1
        db.close()

        Button(self.window, text='Return', command=self.onReturn).grid(row=4, column=1, pady=(310, 10))

    def onReturn(self): 
        self.quitWindow()