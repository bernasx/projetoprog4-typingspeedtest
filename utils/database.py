import sqlite3
class Database:
    def __init__(self):
        con = sqlite3.connect('./utils/database.db')
        cur = con.cursor()
        self.con = con
        self.cur = cur
    
    def close(self):
        self.con.close()
    
    def writeQuery(self, str):
        self.cur.execute(str)
        self.con.commit()
    
    def fetchAllQuery(self, str):
        self.cur.execute(str)
        return self.cur.fetchall()