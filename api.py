from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "mydb"


mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customers")
    customers = cur.fetchall()
    cur.close()

    return render_template('index.html', customers=customers)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        last_name = request.form['last_name']        
        first_name = request.form['first_name']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        country = request.form['country']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customers (last_name, first_name, email, phonenumber, country) VALUES (%s, %s, %s, %s, %s)", (last_name, first_name, email, phonenumber, country))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))