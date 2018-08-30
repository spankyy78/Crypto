# Crypto

This project is a web application which allow you to subscribe to notification 
about crypto money. For some exemple, you can set it up to receive by email a 
notification when BTC falls under 5000$. This web application use coinbase API 
in order to do that.

To launch the application localy, you have to be in a python virtual
environment with python 2.X and Django 1.X or later versions. Then, go to the
manage.py location and execute the following commands:

shell$ ./manage.py makemigrations
shell$ ./manage.py migrate
shell$ ./manage.py runserver

Your server is now launched on localhost with port 8000. In order to use the
app, simply launch your browser and go the this address:

localhost:8000/

You can now use the web applications fonctionnalities.
