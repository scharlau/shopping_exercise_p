# Shopping Exercise in Python with Flask, Sqlite3 and SQLAlchemy
A shopping example in python as a deliberate practice exercise

## Background

This version uses basic bootstrap https://getbootstrap.com for styling and other flask extensions in order to highlight their implementation. This means the application has more folders and files than other examples.

The main launching file, shopping.py is mostly empty, and calls code in the app/__ini__.py file. While you might think the database needs to be in the 'app' folder, this is not the case. It needs to be in the root folder given its current path.

The application uses DynaConf https://www.dynaconf.com to manipulate TOML files, which hold application configuration settings, which mean we don't need to put 'secret' keys into the code for you to read on GitHub, but rather can separate those out to be called from local files instead. This makes our application more secure, and if we're working in a team, then we can each set things up to suit us, without having to worry about changes affecting the repository. Install dynaconf with the command

        pip install dynaconf

We can use dynaconf to provide the secret key needed for the Flask Debug Toolbar https://github.com/flask-debugtoolbar/flask-debugtoolbar, which will help development. Install this with the command

        pip install flask-debugtoolbar

To use the flask-debugtoolbar we need to generate a secret key, which is stored in the .secrets.toml file. You can read more about TOML at https://toml.io/en/ Start the python interpreter and then add these commands:
        python3
        >>> import secrets
        >>> print(secrets.token_hex(24))
        <' generated secret key '>
        exit()

Copy the string that is generated and paste it into .secrets.toml, which you store in the root directory. It should look like this:

        [default]
        secret_key="your secret key string"

The '.secrets.toml' file is where you can also put API keys and other values, which should not be held in the version control system. Instead, put a sample version in with instructions for new contributors, so that they can configure their settings as needed.

In the root folder you also need a settings.toml file for the flask-debugtoolbar to read its values. That should look like this:

        [default]

        [development]
        flask_debug= true
        extensions=["flask_debugtoolbar:DebugToolbarExtension"]
        debug_tb_enabled = true
        debug_tb_intercept_redirects = false

        [production]
        flask_debug = false

While this example has nothing secret in it, you might want to keep it out of the version control repository, and only put in a 'sample' placeholder version for new contributors to see. The one here has nothing special, so is added to the repo.

With dynaconf and flask-debugtoolbar settings in place, when we start the app now we'll see a menu on the right with debug information. This can be minimised, and will aid in debugging/developing the application further.

This app is also set up to use Python logging with configurations set up via a YAML file, which can be read with the Pyyaml library. Install that with 

        pip install pyyaml

You'll find the logging_config.yaml file in the root, which reads values from settings.toml, and examples of how it's used in both the shopping.py and app/__ini__.py files. This makes it easier to manage confirmation of values by sending them to the logger instead of using print(something) statements, which might accidently get into production.

You will also need a number of other libraries added for this example that deal with the database, login, encryption (generating hashes of passwords), and a few other things.

https://pypi.org/project/SQLAlchemy/1.4.21/ 
https://flask-migrate.readthedocs.io/en/latest/ 
https://flask-login.readthedocs.io/en/latest/
https://flask-bcrypt.readthedocs.io/en/latest/

        pip install SQLAlchemy==1.4.21
        pip install Flask-Migrate
        pip install flask-login
        pip install flask-bcrypt

With these in place we now have an application that can demonstrate how to set up sessions in Flask, and explore how we might enable a user account system, plus a shopping cart, and then purchases too. We do this by adding an ORM system to the database, a tool to handle migrations (changes) in the database from our code, and then the login and encryption components.

This is NOT a proper shopping site, but an example of how one could be done. The purpose of this is to let you explore how you retrieve and display the information that you want to show on the pages of the site. That means the page styling is minimal, whatever bootstrap provides 'out of the box'.

The goal of 'deliberate practice' is to think about how you'd solve this challenge, and to work at developing code to make this work. There is no single 'correct' version of this code. The purpose of the exercise it become familiar with different ways of making the application work. You should explore how this simple application is done in Rails so that you understand how variables in controllers are show up in the views you see in the browser.

Under 'deliberate practice' we offer up the challenge, then think about options for developing a solution, and code for 12 minutes. After that we pause to discuss how people are approaching the problem, and what they're trying to do. This should be repeated three times and then wrapped up with time for people to express what they found most useful during the session. This should take an hour.

We can now add in some random content for the shopping application using the Faker library from https://pypi.org/project/Faker/. Install Faker with the command: 

        pip install Faker

Now we can use Faker to generate customer and product details in the in the 'setup_db.py' file. Go to https://faker.readthedocs.io/en/stable/providers.html and look through the options for Standard Providers to see if you want to change any details in values used.

## Setting up the Exercise
Pull this Git repository into your system so that you have everything to get you started.

Run the setup_db.py file to create the tables, and load the generated data into your tables. This will generate customers with addresses, items in your catalogue, and orders by customers.

Load the application settings into your terminal and start the server with 

        export FLASK_APP=shopping.py 
        export FLASK_ENV=development
        python3 -m flask run 

##  Doing the Work

Work through the three rounds with a partner, or on your own, depending upon your circumstances. Each round should be twelve minutes, followed by a discussion of where you are and what has been working, as well as, what you're working on next.

You may want to refer to the setup_db.py file to understand the database schema before you get started. Some of you might even want to diagram the schema. 

You might also want to spend a few minutes at the start of each round planning what you might want to do.

You'll see that this version works with SQL queries and statements to manipulate the data we display on the page. This means we're working with tuples returned to us from the database, which force us to do things in certain ways. You can see this in the html pages that display the data. Look at the SQL python documentation page for more details https://docs.python.org/3/library/sqlite3.html

1. Round one should be fixing the order_detail.html page to show names of items and customers, who placed the order. If you have time, then you can also fix the customer_details.html page to show the customer's orders, and let them click through to the order_details.html page. As you can see the solution here goes beyond this and adds detail pages for customers too, and adds a base.html file to more easily enable navigation.
2. Round two should be creating a 'dashboard' page to show total orders ranked by customers.
3. Round three is making round two work when you scale up the database by changing the numbers in the loops for the setup_db.py file to work with 50 customers and orders of 10 items per customer.
4. Round four, would apply Python models to tuck the SQL away from the main application, and remove some of the duplication. 
