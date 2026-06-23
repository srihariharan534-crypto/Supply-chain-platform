-- Supply Chain Platform Star Schema Definition

-- Dimension: Time
CREATE TABLE IF NOT EXISTS dim_time (
    time_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_actual DATE NOT NULL,
    year INTEGER NOT NULL,
    quarter INTEGER NOT NULL,
    month INTEGER NOT NULL,
    week_of_year INTEGER NOT NULL,
    day_of_month INTEGER NOT NULL,
    day_of_week INTEGER NOT NULL,
    is_weekend BOOLEAN NOT NULL
);

-- Dimension: Product
CREATE TABLE IF NOT EXISTS dim_product (
    product_id VARCHAR(50) PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    subcategory VARCHAR(100),
    unit_price DECIMAL(10, 2),
    weight_kg DECIMAL(10, 2),
    volume_m3 DECIMAL(10, 2)
);

-- Dimension: Warehouse
CREATE TABLE IF NOT EXISTS dim_warehouse (
    warehouse_id VARCHAR(50) PRIMARY KEY,
    warehouse_name VARCHAR(255) NOT NULL,
    location_city VARCHAR(100) NOT NULL,
    location_country VARCHAR(100) NOT NULL,
    capacity_m3 DECIMAL(15, 2),
    manager_name VARCHAR(100)
);

-- Dimension: Supplier
CREATE TABLE IF NOT EXISTS dim_supplier (
    supplier_id VARCHAR(50) PRIMARY KEY,
    supplier_name VARCHAR(255) NOT NULL,
    country VARCHAR(100) NOT NULL,
    risk_rating VARCHAR(50),
    average_lead_time_days INTEGER,
    contract_status VARCHAR(50)
);

-- Fact: Inventory
CREATE TABLE IF NOT EXISTS fact_inventory (
    inventory_id VARCHAR(50) PRIMARY KEY,
    time_id INTEGER,
    product_id VARCHAR(50),
    warehouse_id VARCHAR(50),
    quantity_on_hand INTEGER,
    reorder_point INTEGER,
    safety_stock INTEGER,
    unit_cost DECIMAL(10, 2),
    total_value DECIMAL(15, 2),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (warehouse_id) REFERENCES dim_warehouse(warehouse_id)
);

-- Fact: Logistics
CREATE TABLE IF NOT EXISTS fact_logistics (
    shipment_id VARCHAR(50) PRIMARY KEY,
    dispatch_time_id INTEGER,
    arrival_time_id INTEGER,
    supplier_id VARCHAR(50),
    destination_warehouse_id VARCHAR(50),
    status VARCHAR(50),
    transport_cost DECIMAL(10, 2),
    carrier_name VARCHAR(100),
    delay_days INTEGER,
    FOREIGN KEY (dispatch_time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (arrival_time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (supplier_id) REFERENCES dim_supplier(supplier_id),
    FOREIGN KEY (destination_warehouse_id) REFERENCES dim_warehouse(warehouse_id)
);

-- Fact: Demand
CREATE TABLE IF NOT EXISTS fact_demand (
    demand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_id INTEGER,
    product_id VARCHAR(50),
    sales_quantity INTEGER,
    revenue DECIMAL(15, 2),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id)
);
