# Shopping Exercise in Python with Flask and Sqlite3
A shopping example in python as a deliberate practice exercise

The goal of 'deliberate practice' is to think about how you'd solve this challenge, and to work at developing code to make this work. There is no single 'correct' version of this code. The purpose of the exercise it become familiar with different ways of making the application work. You should explore how this simple application is done in Rails so that you understand how variables in controllers are show up in the views you see in the browser.

Under 'deliberate practice' we offer up the challenge, then think about options for developing a solution, and code for 12 minutes. After that we pause to discuss how people are approaching the problem, and what they're trying to do. This should be repeated three times and then wrapped up with time for people to express what they found most useful during the session. This should take an hour.

We can now add in some random content for the shopping application using the Faker library from https://pypi.org/project/Faker/. Install Faker with the command: 

        pip install Faker

Now we can set about changing the nouns, adjectives and other parts of mystory with values from Faker. Go to https://faker.readthedocs.io/en/stable/providers.html and look through the options for Standard Providers to see if you want to change any details in values used in setup_db.py.

## Setting up the Exercise
Pull this Git repository into your system so that you have everything to get started.

Run the setup_db.py file to load the Faker data into your tables.

Load the application settings into your terminal and start the server with 

        export FLASK_APP=?????.py 
        export FLASK_ENV=development
        python3 -m flask run 

