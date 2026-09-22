"""
products.py
CRUD operations for the products table.
"""

from database import execute_query, fetch_query


def add_product(name, category, price):
    query = "INSERT INTO products (product_name, category, unit_price) VALUES (%s, %s, %s)"
    execute_query(query, (name, category, price))
    print(f"Product '{name}' added successfully.")


def view_products():
    rows = fetch_query("SELECT product_id, product_name, category, unit_price FROM products")
    print("\n--- Product List ---")
    print(f"{'ID':<5}{'Name':<20}{'Category':<15}{'Price':<10}")
    for pid, name, category, price in rows:
        print(f"{pid:<5}{name:<20}{category:<15}{price:<10}")


def delete_product(product_id):
    execute_query("DELETE FROM products WHERE product_id = %s", (product_id,))
    print(f"Product {product_id} deleted (if it existed).")
