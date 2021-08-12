# Question-Paper-Webapp
It acts as  repository to store and fetch needed question papers of previous batch.

Question paper web app :

A web app that serves as a repository for students to access their question papers from previous batches.
We used flask server and sqlite to develop this.

Working :

Previously if an application required an database, i used mysql as my database...but to set it up and manage we needed a sql server.The problem i really see is its portability.we can't simply package your software and database and hand it over to someone else to utilise. They would need to either access the database from your server (binding you to server and database maintenance) or instal the MySQL database engine on their own server, adjust the settings, and import your database in order to execute your app.

SQLite database is a single file that can be written to any  storage or emailed to a colleague.Moreover we dont need to install sqlite its in the python  standard library. Only thing that we need to do before performing any operations on sqlite database is to open a connection  to an sqlite database file.

Moving onto project execution…I uploaded the data for database from a csv file,
First, we creates the table on sqlite. The sqlite3 tool uses the first row of the CSV file as the names of the columns of the table.
Second, the sqlite3 tool import data from the second row of the CSV file into the table.
First, set the mode to CSV to instruct the command-line shell program to interpret the input file as a CSV file. To do this, you use the .mode command as follows:
sqlite> .mode csv
Second, use the command “.import FILE TABLE” to import the data from the city.csv file into the cities table.
sqlite>.import c:/sqlite/city.csv cities
In the flask in order to get your webapp running, i created static file ie. conn.py, here in this file,
      I created an connection to the database file. And then we set con.row_factory = sqlite3.Row  so you can have name-based access to columns.(So now, when you pull rows from your database, you won't get back a plain python tuple, but a special object that makes it easier to work with (e.g. allowing you to access columns using names whereas a plain tuple would make you use numbered indices).)
So far i created a databse and inserted data using csv,  and created a .py  file to open the database and access  the data in it and using render_template() we open the necessary html file, where students will search for qpapers.
Now we need a html file as UI for searching into the database,Initially I developed an html page...containing only search bar for students to search the subject they want…..and display the contents they searched for. Its made with html and css styling. The contents we type.search in the html file will be,passed to the .py file using name of the searh bar and searched using cursor object in the database.
The cursor is used to traverse the records from the result set. We call the execute() method of the cursor and execute the SQL statement, after fetching required data from the database we have to display the data into the webpage...using render_template we return the fetched data but we cant directly dislay the data into table, as html dont have loops to traverse the provided file, so we use jinja(which allow as to write programming inside markup lanfuage), to traverse the given data and display the content.
Now the full project is compete, how we run the project is, run the conn.py file which will run the flask server and render search.html file in browser,which asks for what subject it has to search in html file, after typed for certain subject, the searched subject nme will be collected by connpy file using the search bar name, and then it creates an cnnection to the database file and creates a cursor to traverse the database and perform operation on it, compare the subject entered by the student with the database and fetch all the matching results in it and  store it in a variable, and render the search.html page with the variable, and display the contents there using jinja, in the table format.
