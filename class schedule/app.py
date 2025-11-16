from flask import Flask, request, render_template
import sqlite3

con = sqlite3.connect("database.db")
cr = con.cursor()

cr.execute("create table if not exists user(t_name TEXT, c_name TEXT, password TEXT, num TEXT, time TEXT, sub TEXT, Date TEXT, grade TEXT)")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/View')
def View():
    return render_template('View.html')

@app.route('/schedule', methods=['POST', 'GET'])
def schedule():
    if request.method == 'POST':
        data = request.form
        List = []
        for key in data:
            List.append(data[key])
        print(List)

        con = sqlite3.connect("database.db")
        cr = con.cursor()
        cr.execute("insert into user values(?,?,?,?,?,?,?,?)", List)
        con.commit()

        return render_template('index.html', msg="Class scheduled successfully..")
    return render_template('index.html')

@app.route('/display', methods=['POST', 'GET'])
def display():
    if request.method == 'POST':
        Date = request.form['Date']
        con = sqlite3.connect("database.db")
        cr = con.cursor()
        cr.execute("select * from user where date = '"+Date+"'")
        result = cr.fetchone()
        print(result)
        if result:
            return render_template('View.html', result=result)
        else:
            return render_template('View.html', msg="There is no any class on this date")
    return render_template('View.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
