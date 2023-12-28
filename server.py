from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(1, 8)


@app.route("/")
def home_page():
    return ('<h1> Guess a number between 0 and 9 </h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route("/<int:number>")
def user_guess(number):
    if number > random_number:
        return ('<h1> Too high, try again! </h1> '
                '<img src="https://media.giphy.com/media/ijgLeINIH40Jor6TD1/giphy.gif">')
    elif number < random_number:
        return('<h1> Too low, try again! </h1> '
               '<img src="https://media.giphy.com/media/t3cL1iKETUqlBaQ6YV/giphy.gif">')
    else:
        return('<h1> You got it right! </h1> '
               '<img src="https://media.giphy.com/media/TdfyKrN7HGTIY/giphy.gif">')


app.run(debug=True)