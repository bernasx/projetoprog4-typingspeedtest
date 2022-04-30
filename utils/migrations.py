import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE games
               (date text, player text, wpm real, cpm real)''')
con.commit()
con.close()