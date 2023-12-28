from flask import Flask

app = Flask(__name__)


# Basic Routing to send to home page
@app.route("/")
def say_hello():
    return ("<h1 style='text-align : center'> Hello World! </h1> "
            "<p>Hope you are having a great day!</p>"
            "<img src='https://media.giphy.com/media/LPQ943m8yMcpy/giphy.gif' width=500px class='center'>")
    # Flask accepts HTMl in the return statement


# Use Variable Routing to add a variable in the decorator and use it in the function
@app.route("/username/<name>/<int:number>")
def greeting(name, number):
    return f"Hello, {name}, you are {number} years old."


def make_bold(function):
    def wrapper():
        end_text = function()
        return f"<b> {end_text} </b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        end_text = function()
        return f"<em> {end_text} </em>"
    return wrapper


@app.route("/bye")
@make_bold
@make_emphasis
def say_bye():
    return "Bye!"


