# Shopping Exercise in Python with Flask and Sqlite3
A shopping example in python as a deliberate practice exercise

This is NOT a proper shopping site, but the back end of what one could be. It is missing the authentication and security aspects that you'd expect. The purpose of this is to let you explore how you retrieve and display the information that you want to show on the pages of the site.

The goal of 'deliberate practice' is to think about how you'd solve this challenge, and to work at developing code to make this work. There is no single 'correct' version of this code. The purpose of the exercise it become familiar with different ways of making the application work. You should explore how this simple application is done in Rails so that you understand how variables in controllers are show up in the views you see in the browser.

Under 'deliberate practice' we offer up the challenge, then think about options for developing a solution, and code for 12 minutes. After that we pause to discuss how people are approaching the problem, and what they're trying to do. This should be repeated three times and then wrapped up with time for people to express what they found most useful during the session. This should take an hour.

We can now add in some random content for the shopping application using the Faker library from https://pypi.org/project/Faker/. Install Faker with the command: 

        pip install Faker

Now we can use Faker to generate customer and product details in the in the 'setup_db.py' file. Go to https://faker.readthedocs.io/en/stable/providers.html and look through the options for Standard Providers to see if you want to change any details in values used.

## Setting up the Exercise
Pull this Git repository into your system so that you have everything to get started.

Run the setup_db.py file to create the tables, and load the generated data into your tables.

Load the application settings into your terminal and start the server with 

        export FLASK_APP=shopping.py 
        export FLASK_ENV=development
        python3 -m flask run 

##  Doing the Work

Work through the three rounds with a partner, or on your own, depending upon your circumstances. Each round should be twelve minutes, followed by a discussion of where you are and what has been working, as well as, what you're working on next.

You may want to refer to the setup_db.py file to understand the database schema before you get started. Some of you might even want to diagram the schema. 

You might also want to spend a few minutes at the start of each round planning what you might want to do.

You'll see that this version works with SQL queries and statements to manipulate the data we display on the page. This means we're working with tuples returned to us from the database, which force us to do things in certain ways. You can see this in the html pages that display the data. Look at the SQL python documentation page for more details https://docs.python.org/3/library/sqlite3.html

1. Round one should be fixing the order_detail.html page to show names of items and customers, who placed the order. If you have time, then you can also fix the customer_details.html page to show the customer's orders, and let them click through to the order_details.html page.
2. Round two should be creating a 'dashboard' page to show total orders ranked by customers.
3. Round three is making round two work when you scale up the database by changing the numbers in the loops for the setup_db.py file to work with 50 customers and orders of 10 items per customer.
4. Round four, would apply Python models to tuck the SQL away from the main application, and remove some of the duplication. 
