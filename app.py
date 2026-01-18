from flask import Flask

# Flaskの初期化
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello Sparta Camp!!</h1>"


@app.route("/goodbye")
def goodbye():
    return "Goodbye!!!???"


@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello, {name}!</h1>"


if __name__ == "__main__":
    app.run(port=8000, debug=True)
