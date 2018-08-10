# Database-functionalities
This repository will be a basic tutorial on using sqlite3. 
## Getting Started
Clone this repository and tinker with the functions to start off. 
### Prerequisites
* Sqlite3 (database management system)
* DB Browser (Visualization tool for databases)
### Installation
Sqlite3 already comes pre-installed  with python3. To get DB browser, you can visit the following website - 
https://sqlitebrowser.org/

## Tutorial 
In this tutorial, we will cover the following topics - 
* What is sqlite3
* Making a database
* Making tables
* Putting data into a database
* Reading values from a database
* Updating or deleting values from a database

**NOTE** - While going through the topics above, there will be many parts of sqlite3 that I cover on the way. To gain full understanding of sqlite, I recommend going through the tutorial in order. 
### What is sqlite3
Well, as the name says it, it's *lite*. Sqlite is a module provided in Python to make very small databases. The database can be stored on disk or even RAM. Sqlite is an alternative to very big database applications like *mysql*. 

### Making a database
Turns out, it we try to connect to a database that doesn't exist, sqlite3 makes one for us. Heres what I mean - 

    conn = sqlite3.connect("movieData.db")
The following code, connects to a database. A connection is a way of specifying which database you want to work with. For example, if I want to put additional data in movieData.db, I will have to connect to it first. But, if the database doesn't exist, then a new database with the name movieData.db is made.
### Making tables
Before we can manipulate a database in any way, we need to make a cursor. Once we connect to a database, we need to make a cursor for the connected database. A cursor in a database can be visualized as an actual cursor. We can move the cursor and make it do things for us in the database. To make a cursor, we run the following command on the previously initialized connection - 

    c = conn.cursor()


Now that we have a cursor, we can get rolling. Our first step is to make a table. This table has headers, and we can put in multiple rows as data. To make a table, run the following command -
    
     c.execute('CREATE TABLE IF NOT EXISTS plots(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

By convention, sqlite commands are written in CAPS. The command above only makes a table using the cursor, if the table does not exist. This logic is very important and should be included in your programs. If a table already has data, and you make another empty table with the same name, all the data will be lost. 

Lets break down what the command above is doing in detail - 

* **CREATE TABLE** - This command is used to make a new table
* **IF NOT EXISTS** - Piece of logic to make sure to only create a new table if it doesn't exist
* **plots** - This is the name of the new table
* **unix, datestamp, keyword, value** - These are the names of my headers, or columns. My data will fall under these categories
* **REAL, TEXT** - These are used to specify what kind of data type will be put in a column. Example - datestamp will only store text


### Putting data into a database 

By now, you should have realized how databases work. The tree diagram below will explain it. 

* Databases 
    * Multiple tables - A database can have many tables 
        * Data - Data can be stored in any of the tables in a database

So, to put data into a database, we need to specify which table to put it into. You can add data by doing the following - 

         c.execute("INSERT INTO plots VALUES(342341, '2018-08-02', 'first', 5)")
         conn.commit()
         
We execute a command using the cursor. In this case, we add data into the table plots. We use **VALUES()** to specify the values we want to add to the database. After we finish doing so, we need to commit the changes. This saves the additional work we have done on the database.

It is a little tricky when it comes to using variables when adding data into a table. As programmers, we never want to hand code things that goes into the database. We want to pass variables that hold the data. To do so, we run the following - 

    c.execute("INSERT INTO plots (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (variable1,variable2,variable3,variable4))
    conn.commit()


Notice, everything is the same except for the **?** in **VALUES()**. The question marks act as placeholders. Then, we can specify the variables in parentheses. 

### Reading values from a database

Sqlite is a very powerful tool. We can run various filters to get data or a part of the data we want. We will cover multiple examples to understand how to do so. 

To get all the data at once, we can run the following command - 

    c.execute('SELECT * FROM plots')
    data = c.fetchall()

The first piece of code uses the cursor to select what we want from our table. The * is to select everything from plots. The fetchall() method gets everything we selected. We can select only parts of the data we want. To do so, we replace * with what we want. 

    c.execute('SELECT value FROM plots')
    data = c.fetchall()
This gets the only the column value.

    c.execute("SELECT * FROM plots WHERE value=3 AND keyword='Python'")
    data = c.fetchall()
    
This is an example of a filter to only get the rows of data that have value = 3 and the keyword = Python.

### Updating and deleting values
