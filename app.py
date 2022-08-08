import datetime
import mysql.connector
from flask import Flask,render_template, request

app = Flask(__name__)
class Database:
    def __init__(self):
        host="localhost"
        user="root"
        password="your_password"
        database="your_db_name"
        
        self.con = mysql.connector.connect(host = host, user = user, password = password, database = database)
        self.cur = self.con.cursor()

    def list_employees(self):
        self.cur.execute("SELECT employee.emp_id, employee.firstname, address.city from employee INNER JOIN address on employee.address_id = address.address_id")
        result = self.cur.fetchall()
        return result

    def search_employee(self,emp_id):
        self.cur.execute("SELECT employee.emp_id, employee.firstname, address.city from employee INNER JOIN address on employee.address_id = address.address_id where emp_id = %s", (emp_id,))
        result = self.cur.fetchall()
        print(result)
        return result



@app.route('/')
def employee():
    def db_query():
        db = Database()
        employees = db.list_employees()
        return employees

    res = db_query()

    return render_template("home.html", result = res)
 


@app.route('/search', methods=['POST'])
def search():
    if request.method == "POST":
        def db_query():
            db = Database()
            id =  request.form['id']
            employee = db.search_employee(id)
            return employee

        res = db_query()

    return render_template("home.html", result = res)

