"""
main.py
Console menu that ties products.py, sales.py and analytics.py together.
Run this file to use the app: python main.py
"""

from products import add_product, view_products
from sales import add_sale, print_sales
from analytics import generate_report


def menu():
    while True:
        print("\n==== RETAIL SALES ANALYZER ====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Record a Sale")
        print("4. View All Sales")
        print("5. Generate Analytics Report (NumPy)")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Product name: ")
            category = input("Category: ")
            price = float(input("Unit price: "))
            add_product(name, category, price)

        elif choice == "2":
            view_products()

        elif choice == "3":
            product_id = int(input("Product ID: "))
            quantity = int(input("Quantity sold: "))
            add_sale(product_id, quantity)

        elif choice == "4":
            print_sales()

        elif choice == "5":
            generate_report()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
