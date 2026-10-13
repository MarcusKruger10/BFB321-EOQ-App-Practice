# app.py
from flask import Flask, render_template, request
from eoq import calculate_eoq, total_annual_cost

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', name='BFB321 Student')


@app.route('/about')
def about():
    inputs = [
        {'symbol': 'D', 'meaning': 'Annual demand (units per year)', 'example': '12 000'},
        {'symbol': 'S', 'meaning': 'Ordering cost per order', 'example': 'R50'},
        {'symbol': 'H', 'meaning': 'Holding cost per unit per year', 'example': 'R2'},
    ]
    example_eoq = round(calculate_eoq(12000, 50, 2), 2)
    return render_template('about.html', inputs=inputs, example_eoq=example_eoq)


# methods=['GET', 'POST'] -> this route can show the form AND receive it
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None    # starts empty, so the page shows no answer on GET
    error = None

    if request.method == 'POST':
        # request.form['name'] reads the input with that name attribute.
        # Form values always arrive as STRINGS -> convert with float()
        D = float(request.form['demand'])
        S = float(request.form['ordering_cost'])
        H = float(request.form['holding_cost'])

        # Validate BEFORE calculating (H = 0 would cause ZeroDivisionError)
        if D <= 0 or S <= 0 or H <= 0:
            error = 'All values must be greater than 0.'
        else:
            eoq = calculate_eoq(D, S, H)
            orders = D / eoq
            result = {
                'eoq': round(eoq, 2),
                'orders_per_year': round(orders, 2),
                'days_between': round(365 / orders, 1),
                'total_cost': round(total_annual_cost(D, S, H, eoq), 2),
            }

    return render_template('calculator.html', result=result, error=error)


# Bonus: request.args reads GET data from the URL, e.g. /cost?qty=500
@app.route('/cost')
def cost():
    qty = float(request.args.get('qty', '774.6'))   # default if qty is missing
    total = total_annual_cost(12000, 50, 2, qty)
    return f'Total annual cost for ordering {qty} units: R{round(total, 2)}'


if __name__ == '__main__':
    app.run(debug=True)