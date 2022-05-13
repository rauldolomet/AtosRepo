from crypt import methods
from operator import methodcaller
from flask import Flask
from flask import request
app=Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "hello world"

# @app.route("/greet")
# def greet():
#     return "Hello!"

# @app.route("/greet/<name>")
# def greetName(name):
#     return "Hello, " + name

# @app.route("/bye", methods=['GET'])
# def Bye():
#     print(request.form)
#     return "Draga " + request.form["for"] + ", iti urez " + request.form["wish"]