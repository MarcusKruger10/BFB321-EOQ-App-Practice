# app.py
from flask import Flask, render_template
from eoq import calculate_eoq      # reuse YOUR function from eoq.py

app = Flask(__name__)


@app.route('/')
def home():
    # Pass a variable into the template -> shows up as {{ name }}
    return render_template('index.html', name='BFB321 Student')


@app.route('/about')
def about():
    # A list of dictionaries -> looped over with {% for row in inputs %}
    inputs = [
        {'symbol': 'D', 'meaning': 'Annual demand (units per year)', 'example': '12 000'},
        {'symbol': 'S', 'meaning': 'Ordering cost per order', 'example': 'R50'},
        {'symbol': 'H', 'meaning': 'Holding cost per unit per year', 'example': 'R2'},
    ]
    example_eoq = round(calculate_eoq(12000, 50, 2), 2)
    return render_template('about.html', inputs=inputs, example_eoq=example_eoq)


@app.route('/calculator')
def calculator():
    return render_template('calculator.html')


if __name__ == '__main__':
    app.run(debug=True)