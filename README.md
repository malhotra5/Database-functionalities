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
