"""
analytics.py
This is where NumPy earns its place: we pull raw sales rows from MySQL
(plain Python tuples) and convert the numeric columns into NumPy arrays
so we can do fast, vectorized math instead of manual loops.
"""

import numpy as np
from sales import view_sales


def generate_report():
    data = view_sales()
    if not data:
        print("No sales data available yet. Add some sales first.")
        return

    # Unpack columns into separate NumPy arrays
    product_names = [row[1] for row in data]
    quantities = np.array([row[2] for row in data])
    prices = np.array([row[3] for row in data], dtype=float)

    # Vectorized math: this multiplies element-by-element, no loop needed
    revenues = quantities * prices

    print("\n===== SALES ANALYTICS REPORT =====")
    print(f"Total Transactions      : {len(data)}")
    print(f"Total Units Sold        : {int(np.sum(quantities))}")
    print(f"Total Revenue           : {np.sum(revenues):.2f}")
    print(f"Average Sale Value      : {np.mean(revenues):.2f}")
    print(f"Highest Single Sale     : {np.max(revenues):.2f}")
    print(f"Lowest Single Sale      : {np.min(revenues):.2f}")
    print(f"Std Deviation (revenue) : {np.std(revenues):.2f}")

    # Revenue per product, aggregated with a plain dict (NumPy doesn't
    # group strings natively, so this part stays plain Python)
    product_revenue = {}
    for name, rev in zip(product_names, revenues):
        product_revenue[name] = product_revenue.get(name, 0) + rev

    best_product = max(product_revenue, key=product_revenue.get)
    print(f"Top Selling Product     : {best_product} "
          f"(Revenue: {product_revenue[best_product]:.2f})")

    # Flag any unusually large sale: more than 1.5 std-dev above the mean
    threshold = np.mean(revenues) + 1.5 * np.std(revenues)
    outliers = [
        (name, rev) for name, rev in zip(product_names, revenues) if rev > threshold
    ]
    if outliers:
        print("\nUnusually large sales (possible bulk orders):")
        for name, rev in outliers:
            print(f"  - {name}: {rev:.2f}")
