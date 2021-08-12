from flask import *
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    con = sqlite3.connect("question.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    if request.method == "POST":
        book = request.form['book']
        # search by author or book
        cur.execute("SELECT id,name,year,link from qpaper WHERE name =(?)",(book,))
    #    cur.execute("SELECT * from qpaper")
        con.commit()
        data = cur.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and book == 'all':
            cur.execute("SELECT name, year , link from qpaper")
            con.commit()
            data = cur.fetchall()
        return render_template('search.html', data=data)
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug = True)
