from flask import Flask
import random 
import random


app = Flask(__name__)


@app.route("/")
def index():
    simbols = "234680-_+qwertyuiop\asdfghjkl;'zxcvbnm,./!@#$%^&*1957"

    generated_password = ""

    for i in range(9):
        generated_password += random.choice(simbols)

        print(generated_password)

    return f'<p>{generated_password}</p><h1><a href="/facts/">Next page→ </a></h1>'


@app.route("/facts/")
def facts():
    with open("facts.txt", "r", encoding="utf-8") as file:
        text = file.read()
        facts = text.split("\n\n")
    return f'<p>{random.choice(facts)}</p><h1><a href="/"> ←Previous page</a></h1>'


app.run(debug=True)