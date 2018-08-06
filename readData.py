import sqlite3

#Create connection and cursor
conn = sqlite3.connect("movieData.db")
c = conn.cursor()

def read():
    #Gets everything
    c.execute('SELECT * FROM plots')
    data = c.fetchall()
    #Print rows of data
    for row in data:
        print(row)
    print('done')
    #Only get results with value = 3 and keyword = Python
    c.execute("SELECT * FROM plots WHERE value=3 AND keyword='Python'")
    data = c.fetchall()
    for row in data:
        print(row)
read()

#Close connections
c.close()
conn.close()
