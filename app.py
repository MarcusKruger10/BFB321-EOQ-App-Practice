# app.py
from flask import Flask

app = Flask(__name__)          # creates the application object


@app.route('/')                # route: the URL "/" runs the function below
def home():                    # view function
    return 'Hello, Supply Chain Class!'


@app.route('/about')
def about():
    return 'This page will explain EOQ.'


if __name__ == '__main__':
    app.run(debug=True)        # starts the server at http://127.0.0.1:5000