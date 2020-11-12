import random
import decimal
import sqlite3
from datetime import datetime
from faker import Faker
from faker.providers import address, internet, person

conn = sqlite3.connect('shopping_data.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()
fake = Faker()

# drop the tables - use this order due to foreign keys - so that we can rerun the file as needed without repeating values
conn.execute('DROP TABLE IF EXISTS line_items')
conn.execute('DROP TABLE IF EXISTS carts')
conn.execute('DROP TABLE IF EXISTS orders')
conn.execute('DROP TABLE IF EXISTS products')
conn.execute('DROP TABLE IF EXISTS customers')

#create the tables again - create them in reverse order of deleting due to foreign keys

conn.execute('CREATE TABLE customers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, address TEXT, created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL)')
conn.execute('CREATE TABLE products ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL)')
conn.execute('CREATE TABLE carts (id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER, quantity INTEGER, created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, FOREIGN KEY(product_id) REFERENCES products(id) )')
conn.execute('CREATE TABLE orders ( id INTEGER PRIMARY KEY AUTOINCREMENT, customer_id INTEGER, created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, FOREIGN KEY(customer_id) REFERENCES customers(id) )')
conn.execute('CREATE TABLE line_items ( id INTEGER PRIMARY KEY AUTOINCREMENT, quantity INTEGER, product_id INTEGER, cart_id INTEGER, order_id INTEGER, created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, FOREIGN KEY(product_id) REFERENCES products(id), FOREIGN KEY(cart_id) REFERENCES carts(id), FOREIGN KEY(order_id) REFERENCES orders(id) )')

# create some customers
for i in range(10):
    name = fake.name()
    email = fake.ascii_free_email()
    address = fake.address()
    cur.execute('INSERT INTO customers VALUES(NULL,?,?,?,?)', (name, email, address, datetime.now()))
    conn.commit()

# create some products
for i in range(10):
    name = fake.catch_phrase()
    price = int( decimal.Decimal(random.randrange(155,899))/100)
    cur.execute('INSERT INTO products VALUES(NULL,?,?,?)', (name, price, datetime.now()))
    conn.commit()

# create some carts 
cur.execute('select * from products')
products = cur.fetchall()
product_id_list = []
for product in products:
    product_id_list.append(product[0])

for i in range(10):
    random_id = random.randint(1,9)
    product_id = product_id_list[random_id]
    quantity = random.randrange(1,42)
    cur.execute('INSERT INTO carts VALUES(NULL,?,?,?)', (product_id, quantity, datetime.now()))
    conn.commit()

# create orders from customers
cur.execute('select * from customers')
customers = cur.fetchall()
for customer in customers:  
    for i in range(3):
        customer_id = customer[0]
        # note that need trailing comma in the sql statement
        cur.execute('INSERT INTO orders VALUES(Null,?,?)', (customer_id, datetime.now()))
        conn.commit()

# attach line_items to orders
cur.execute('select * from orders')
orders = cur.fetchall()

cur.execute('select * from carts')
carts = cur.fetchall()

for order in orders:
    for cart in carts:
        quantity = cart[2]
        product_id = cart[1]
        cart_id = cart[0]
        order_id = order[0]
        cur.execute('INSERT INTO line_items VALUES(NULL,?,?,?,?,?)', (product_id, quantity, cart_id, order_id, datetime.now()))
        conn.commit()
    

