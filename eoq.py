# eoq.py
# EOQ model - interactive version

import math


# ----- Functions (unchanged - Flask will reuse these) -----
def calculate_eoq(demand, order_cost, hold_cost):
    """Return the Economic Order Quantity."""
    return math.sqrt((2 * demand * order_cost) / hold_cost)


def total_annual_cost(demand, order_cost, hold_cost, order_qty):
    """Return ordering cost + holding cost for a given order quantity."""
    ordering = (demand / order_qty) * order_cost
    holding = (order_qty / 2) * hold_cost
    return ordering + holding


# Everything below only runs when you run THIS file directly.
# When Flask imports the functions above, this part is skipped.
if __name__ == "__main__":
    again = "y"

    # ----- While loop: keep going until the user says no -----
    while again == "y":
        print("\n=== EOQ Calculator ===")

        # ----- input() always returns a STRING, so cast with float() -----
        demand = float(input("Annual demand (D): "))
        order_cost = float(input("Ordering cost per order (S): R"))
        hold_cost = float(input("Holding cost per unit per year (H): R"))

        # ----- Validation: logical operator 'or' + if/else -----
        if demand <= 0 or order_cost <= 0 or hold_cost <= 0:
            print("Error: all values must be greater than 0.")
        else:
            eoq = calculate_eoq(demand, order_cost, hold_cost)
            orders_per_year = demand / eoq

            # ----- Dictionary: key -> value pairs -----
            results = {
                "Optimal order quantity": round(eoq, 2),
                "Orders per year": round(orders_per_year, 2),
                "Days between orders": round(365 / orders_per_year, 1),
                "Total annual cost (R)": round(total_annual_cost(demand, order_cost, hold_cost, eoq), 2),
            }

            # ----- For loop over the dictionary with .items() -----
            for label, value in results.items():
                print(label + ":", value)

            # ----- Chained conditional: if / elif / else -----
            if orders_per_year > 12:
                print("Advice: you'll order more than once a month.")
            elif orders_per_year >= 4:
                print("Advice: you'll order roughly every 1 to 3 months.")
            else:
                print("Advice: you'll order fewer than 4 times a year.")

        # ----- String methods: .strip() removes spaces, .lower() fixes "Y" -----
        again = input("\nCalculate another? (y/n): ").strip().lower()

    print("Goodbye!")
