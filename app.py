from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("dit wil ik in de console")
    print("een extra zin")
    return "Dan gaat dit terug naar de Browser"