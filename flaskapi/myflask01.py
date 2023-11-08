#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   A simple Flask server. Responds to HTTP 'GET /' requests
   with a 'Hello World' attached to a 200 response"""


# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hello_world_sb():
   return "Goooooood Morning World and all who inhabit it!"

#option 1
@app.route("/hello")
def hello_world():
    return "hello world"

#option 2
def hello_world2():
    return "hello world again"
app.add_url_rule("/hello2", "hello2", hello_world2)

@app.route("/characters")
def characters():
    return "Ned Stark is a lawful good cookie"

@app.route("/favorite")
def favorite():
    return {"1":"Eddard Stark", "2":"Rob Stark", "3":"Sansa Stark", "4":"Oberyn Martell"}

if __name__ == "__main__":
#   app.run(host="0.0.0.0", port=2224) # runs the application
   app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
