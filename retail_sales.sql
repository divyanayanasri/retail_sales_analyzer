-- Retail Sales Analyzer: schema + sample data
-- Run this whole file in MySQL Workbench or `mysql -u root -p < retail_sales.sql`

CREATE DATABASE IF NOT EXISTS retail_sales_db;
USE retail_sales_db;

-- 1. Products master table
CREATE TABLE IF NOT EXISTS products (
    product_id   INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category     VARCHAR(50)  NOT NULL,
    unit_price   DECIMAL(10,2) NOT NULL
);

-- 2. Sales transactions table (each row = one sale of one product)
CREATE TABLE IF NOT EXISTS sales (
    sale_id     INT AUTO_INCREMENT PRIMARY KEY,
    product_id  INT NOT NULL,
    quantity    INT NOT NULL,
    sale_date   DATE NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- 3. Sample products
INSERT INTO products (product_name, category, unit_price) VALUES
('Wireless Mouse',    'Electronics', 499.00),
('Bluetooth Speaker',  'Electronics', 1299.00),
('Notebook Pack',      'Stationery',  120.00),
('Office Chair',       'Furniture',   3499.00),
('LED Desk Lamp',      'Furniture',   899.00);

-- 4. Sample sales spread across a few dates (so trends show up)
INSERT INTO sales (product_id, quantity, sale_date) VALUES
(1, 3, '2026-09-01'),
(2, 1, '2026-09-02'),
(3, 10, '2026-09-02'),
(1, 5, '2026-09-05'),
(4, 2, '2026-09-06'),
(5, 4, '2026-09-07'),
(2, 2, '2026-09-10'),
(3, 20, '2026-09-12'),
(1, 7, '2026-09-15'),
(4, 1, '2026-09-18');
