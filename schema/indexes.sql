-- Indexes for Supply Chain Platform Star Schema

-- Fact Inventory Indexes
CREATE INDEX IF NOT EXISTS idx_fact_inventory_time ON fact_inventory(time_id);
CREATE INDEX IF NOT EXISTS idx_fact_inventory_product ON fact_inventory(product_id);
CREATE INDEX IF NOT EXISTS idx_fact_inventory_warehouse ON fact_inventory(warehouse_id);

-- Fact Logistics Indexes
CREATE INDEX IF NOT EXISTS idx_fact_logistics_dispatch_time ON fact_logistics(dispatch_time_id);
CREATE INDEX IF NOT EXISTS idx_fact_logistics_arrival_time ON fact_logistics(arrival_time_id);
CREATE INDEX IF NOT EXISTS idx_fact_logistics_supplier ON fact_logistics(supplier_id);
CREATE INDEX IF NOT EXISTS idx_fact_logistics_warehouse ON fact_logistics(destination_warehouse_id);
CREATE INDEX IF NOT EXISTS idx_fact_logistics_status ON fact_logistics(status);

-- Fact Demand Indexes
CREATE INDEX IF NOT EXISTS idx_fact_demand_time ON fact_demand(time_id);
CREATE INDEX IF NOT EXISTS idx_fact_demand_product ON fact_demand(product_id);

-- Dimension Lookup Indexes
CREATE INDEX IF NOT EXISTS idx_dim_time_date ON dim_time(date_actual);
CREATE INDEX IF NOT EXISTS idx_dim_product_category ON dim_product(category);
CREATE INDEX IF NOT EXISTS idx_dim_supplier_country ON dim_supplier(country);
CREATE INDEX IF NOT EXISTS idx_dim_supplier_risk ON dim_supplier(risk_rating);
