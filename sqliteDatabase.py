import sqlite3
import time
import datetime
import random

#Connect to a database. If it doesn't exist then a new database is made
conn = sqlite3.connect("movieData.db")
#Make a cursor for the database
c = conn.cursor()

def create_table():
    #Creates a new table. You don't want to keep calling this. So some logic has been put into the statement.
    #Execute makes the cursor do something
    c.execute('CREATE TABLE IF NOT EXISTS plots(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
def addData():
    #This inserts values into the table. The order of the values matter
    c.execute("INSERT INTO plots VALUES(342341, '2018-08-02', 'first', 5)")
    #Commit to save the changes
    conn.commit()
def dynamicEntry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H: %M: %S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    #This inserts the variables above into the database
    c.execute("INSERT INTO plots (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()

def update(updateVal, initialVal):
    #All updates are permanent in the database
    #Updating values in a database
    c.execute('UPDATE plots SET value=(?) WHERE value = (?)', (updateVal, initialVal))
    #Committing changes
    conn.commit()

def visualize():
    #Printing everything in the database
    c.execute('SELECT * FROM plots')
    #One line for statement for printing every row in the database
    [print(i) for i in c.fetchall()]
def delete(delVal):
    c.execute('DELETE FROM plots WHERE value = (?)', (delVal,))
    conn.commit()


create_table()
addData()

for _ in range(10):
    dynamicEntry()
    time.sleep(1)
    
update(100,4)
visualize()
print('######################################################################')
delete(100)
visualize()
c.close()
conn.close()
