# from flask import Flask
# from flask import request
from app import create_app

if __name__=='__main__':
    create_app()
 #app=Flask(__name__)

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