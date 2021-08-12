#import sqlite3

#con = sqlite3.connect("question.db")
#print("Database opened successfully")

#con.execute("create table qpaper (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, year INTEGER , link VARCHAR(2083)NOT NULL)")
from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");
#@app.route("/")
#def index():
#    return render_template("search.html");


@app.route("/add")
def add():
    return render_template("add.html")

#@app.route('/', methods=['GET', 'POST'])
#def search():
    con = sqlite3.connect("question.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    if request.method == "POST":
        book = request.form['book']
        # search by author or book
    #    cur.execute("SELECT name,year,link from qpaper WHERE name =?", (book))
        cur.execute("SELECT * from qpaper")
        con.commit()
        data = cur.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and book == 'all':
            cur.execute("SELECT name, year , link from qpaper")
            con.commit()
            data = cur.fetchall()
        return render_template('search.html', data=data)
    return render_template('search.html')

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            year = request.form["year"]
            link = request.form["link"]
            with sqlite3.connect("question.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into qpaper (name, year, link) values (?,?,?)",(name,year,link))
                con.commit()
                msg = "Employee successfully Added"
        except:
            con.rollback()
            msg = "We can not add the employee to the list"
        finally:
            return render_template("success.html",msg = msg)
            con.close()

@app.route("/view")
def view():
    con = sqlite3.connect("question.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from qpaper")
    rows = cur.fetchall()
    return render_template("view.html",rows = rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord",methods = ["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("question.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from qpaper where id = ?",id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html",msg = msg)

if __name__ == "__main__":
    app.run(debug = True)
