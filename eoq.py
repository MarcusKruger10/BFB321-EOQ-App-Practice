# eoq.py
# EOQ model - from the EOQ Tutorial (Supply Chain Technology)

import math   # Refresher 2: imports - gives us math.sqrt()


# ----- Functions (Refresher 2: def, parameters, return) -----
def calculate_eoq(demand, order_cost, hold_cost):
    """Return the Economic Order Quantity."""
    return math.sqrt((2 * demand * order_cost) / hold_cost)


def total_annual_cost(demand, order_cost, hold_cost, order_qty):
    """Return ordering cost + holding cost for a given order quantity."""
    ordering = (demand / order_qty) * order_cost
    holding = (order_qty / 2) * hold_cost
    return ordering + holding


# ----- Inputs (Refresher 1: variables and assignment) -----
annual_demand = 12000   # D - units per year (int)
ordering_cost = 50      # S - Rand per order (int)
holding_cost = 2        # H - Rand per unit per year (int)

# ----- Calculations -----
eoq = calculate_eoq(annual_demand, ordering_cost, holding_cost)
orders_per_year = annual_demand / eoq
days_between_orders = 365 / orders_per_year
cost_at_eoq = total_annual_cost(annual_demand, ordering_cost, holding_cost, eoq)

# ----- Output (Refresher 1: print; Refresher 2: round) -----
print("Optimal order quantity:", round(eoq, 2))
print("Orders per year:", round(orders_per_year, 2))
print("Days between orders:", round(days_between_orders, 1))
print("Total annual cost at EOQ:", round(cost_at_eoq, 2))

# ----- Step 7: prove EOQ is the minimum (Refresher 2: for loop + range) -----
print("\nQty   Total cost")
for qty in range(50, 1500, 100):
    cost = total_annual_cost(annual_demand, ordering_cost, holding_cost, qty)
    print(qty, round(cost, 2))