from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("hello.html")
@app.route("/first")
def first():
    return render_template("first.html")

@app.route("/second")
def second():
    return render_template("second.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")