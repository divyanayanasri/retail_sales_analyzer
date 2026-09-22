# Retail Sales Analyzer

A console-based mini project that combines **MySQL**, **Python**, and **NumPy** —
built while practicing these three topics from my Calibo AI Academy training.

It stores product and sales data in a MySQL database, manages it through a
Python console app, and uses NumPy to generate an analytics report
(total revenue, averages, standard deviation, top-selling product, and
outlier detection).

## Features

- Add and view products (name, category, price)
- Record and view sales, joined with product details
- Generate a NumPy-powered analytics report:
  - Total transactions and units sold
  - Total revenue, average sale value
  - Highest / lowest single sale
  - Standard deviation of revenue
  - Top-selling product by revenue
  - Detection of unusually large ("outlier") sales

## Tech Stack

- **MySQL** – relational storage (`products` and `sales` tables, linked by a foreign key)
- **Python** – application logic and MySQL connectivity (`mysql-connector-python`)
- **NumPy** – vectorized calculations for the analytics report

## Project Structure

```
retail-sales-analyzer/
├── database/
│   └── retail_sales.sql      # Schema + sample data
├── python/
│   ├── database.py           # MySQL connection helper
│   ├── products.py           # Product CRUD
│   ├── sales.py               # Sales CRUD (joined with products)
│   ├── analytics.py          # NumPy-based analytics report
│   └── main.py                # Console menu / entry point
└── requirements.txt
```

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/retail-sales-analyzer.git
   cd retail-sales-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create the database**
   ```bash
   mysql -u root -p < database/retail_sales.sql
   ```

4. **Set your MySQL password**
   Open `python/database.py` and update the `password` field in `DB_CONFIG`.

5. **Run the app**
   ```bash
   cd python
   python main.py
   ```

## Example Menu

```
==== RETAIL SALES ANALYZER ====
1. Add Product
2. View Products
3. Record a Sale
4. View All Sales
5. Generate Analytics Report (NumPy)
6. Exit
```

## What I Practiced

- Designing a relational schema with primary/foreign keys
- Connecting Python to MySQL and separating concerns across modules
- Using NumPy arrays and vectorized operations (`sum`, `mean`, `std`, `max`, `min`)
  instead of manual loops for aggregation
- Basic statistical outlier detection (values beyond 1.5 standard deviations from the mean)

## Next Steps

- Add date-range filtering using NumPy boolean masking
- Move analysis to Pandas for richer grouping and time-series trends
- Add input validation and error handling for invalid menu choices

## License

This is a personal learning project, free to use or adapt.
