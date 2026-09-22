"""
sales.py
Recording new sales and reading them back (joined with product info,
since a sale row only stores product_id + quantity + date).
"""

from datetime import date
from database import execute_query, fetch_query


def add_sale(product_id, quantity, sale_date=None):
    sale_date = sale_date or date.today().isoformat()
    query = "INSERT INTO sales (product_id, quantity, sale_date) VALUES (%s, %s, %s)"
    execute_query(query, (product_id, quantity, sale_date))
    print("Sale recorded successfully.")


def view_sales():
    """Returns rows of (sale_id, product_name, quantity, unit_price, sale_date)."""
    query = """
        SELECT s.sale_id, p.product_name, s.quantity, p.unit_price, s.sale_date
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        ORDER BY s.sale_date
    """
    return fetch_query(query)


def print_sales():
    rows = view_sales()
    print("\n--- Sales List ---")
    for sale_id, name, qty, price, sale_date in rows:
        print(f"#{sale_id} | {name:<20} qty={qty:<3} price={price:<8} date={sale_date}")
