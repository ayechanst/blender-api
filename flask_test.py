from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hellow muthafuka<p>"

    # flask --app flask_test run