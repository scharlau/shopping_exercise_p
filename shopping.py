import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# database details - to remove some duplication
db_name = 'shopping_data.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customers')
def customers():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from customers
    cur.execute("select * from customers")
    rows = cur.fetchall()
    conn.close()
    return render_template('customers.html', rows=rows)

@app.route('/customer_details/<id>')
def customer_details(id):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from customers
    cur.execute("select * from customers WHERE id=?", (id))
    customer = cur.fetchall()
    conn.close()
    return render_template('customer_details.html', customer=customer)

@app.route('/orders')
def orders():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from orders
    cur.execute("select * from orders")
    rows = cur.fetchall()
    conn.close()
    return render_template('orders.html', rows=rows)