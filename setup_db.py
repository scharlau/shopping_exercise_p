import random
import decimal
import sqlite3, datetime
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

conn.execute('CREATE TABLE customers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, address TEXT, created_at timestamp)')
conn.execute('CREATE TABLE products ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, created_at timestamp)')
conn.execute('CREATE TABLE carts (id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER, quantity INTEGER, created_at timestamp, FOREIGN KEY(product_id) REFERENCES products(id) )')
conn.execute('CREATE TABLE orders ( id INTEGER PRIMARY KEY AUTOINCREMENT, customer_id INTEGER, created_at timestamp, FOREIGN KEY(customer_id) REFERENCES customers(id) )')
conn.execute('CREATE TABLE line_items ( id INTEGER PRIMARY KEY AUTOINCREMENT, quantity INTEGER, product_id INTEGER, cart_id INTEGER, order_id INTEGER, created_at timestamp, FOREIGN KEY(product_id) REFERENCES products(id), FOREIGN KEY(cart_id) REFERENCES carts(id), FOREIGN KEY(order_id) REFERENCES orders(id) )')

# create some customers
for i in range(10):
    name = fake.name()
    email = fake.ascii_free_email()
    address = fake.address()
    cur.execute('INSERT INTO customers VALUES(NULL,?,?,?,NULL)', (name, email, address))
    conn.commit()

# create some products
for i in range(10):
    name = fake.catch_phrase()
    price = int( decimal.Decimal(random.randrange(155,899))/100)
    cur.execute('INSERT INTO products VALUES(NULL,?,?,NULL)', (name, price))
    conn.commit()

# create orders from customers
