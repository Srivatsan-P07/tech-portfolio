from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask!</h1>"

@app.route("/username/<name>")
def greet(name):
    return f"<h1> hello, {name}!</h1>"

@app.route("/square/<int:num>")
def square(num):
    square = num * num
    return f"<h1> The square of {num} is {square} </h1>"
    

if __name__ == "__main__":
    app.run(debug=True)