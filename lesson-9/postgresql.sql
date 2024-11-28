CREATE DATABASE store;

CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE NOT NULL,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    sale_amount DECIMAL(10, 2) NOT NULL CHECK (sale_amount >= 0),
    discount DECIMAL(5, 2) DEFAULT 0 CHECK (discount >= 0),
    total_amount DECIMAL(10, 2) GENERATED ALWAYS AS (sale_amount - (sale_amount * discount / 100)) STORED,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO sales (sale_date, customer_id, product_id, quantity, sale_amount, discount)
VALUES
    ('2024-11-01', 1, 101, 2, 100.00, 10.0),  -- 10% discount on $100, total_amount = $90.00
    ('2024-11-02', 2, 102, 1, 50.00, 5.0),    -- 5% discount on $50, total_amount = $47.50
    ('2024-11-03', 1, 103, 3, 30.00, 0.0),    -- No discount on $30, total_amount = $30.00
    ('2024-11-04', 3, 104, 5, 200.00, 15.0),  -- 15% discount on $200, total_amount = $170.00
    ('2024-11-05', 4, 105, 2, 120.00, 20.0);  -- 20% discount on $120, total_amount = $96.00


SELECT * FROM sales;