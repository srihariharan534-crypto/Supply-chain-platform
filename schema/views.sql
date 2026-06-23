-- Views for Supply Chain Platform

-- View: Inventory Health
CREATE VIEW IF NOT EXISTS vw_inventory_health AS
SELECT 
    p.product_name,
    p.category,
    w.warehouse_name,
    i.quantity_on_hand,
    i.reorder_point,
    i.safety_stock,
    (i.quantity_on_hand * i.unit_cost) AS total_value,
    CASE 
        WHEN i.quantity_on_hand <= i.safety_stock THEN 'Critical Stockout Risk'
        WHEN i.quantity_on_hand <= i.reorder_point THEN 'Reorder Needed'
        ELSE 'Healthy'
    END AS inventory_status
FROM fact_inventory i
JOIN dim_product p ON i.product_id = p.product_id
JOIN dim_warehouse w ON i.warehouse_id = w.warehouse_id;

-- View: Supplier Performance
CREATE VIEW IF NOT EXISTS vw_supplier_performance AS
SELECT 
    s.supplier_name,
    s.risk_rating,
    s.average_lead_time_days,
    COUNT(l.shipment_id) AS total_shipments,
    SUM(CASE WHEN l.status = 'Delayed' THEN 1 ELSE 0 END) AS delayed_shipments,
    ROUND(CAST(SUM(CASE WHEN l.status = 'Delayed' THEN 1 ELSE 0 END) AS FLOAT) / NULLIF(COUNT(l.shipment_id), 0) * 100, 2) AS delay_percentage
FROM dim_supplier s
LEFT JOIN fact_logistics l ON s.supplier_id = l.supplier_id
GROUP BY s.supplier_id, s.supplier_name, s.risk_rating, s.average_lead_time_days;

-- View: Logistics Efficiency
CREATE VIEW IF NOT EXISTS vw_logistics_efficiency AS
SELECT 
    l.carrier_name,
    COUNT(l.shipment_id) AS total_shipments,
    AVG(l.delay_days) AS avg_delay_days,
    SUM(l.transport_cost) AS total_transport_cost,
    AVG(l.transport_cost) AS avg_transport_cost_per_shipment
FROM fact_logistics l
GROUP BY l.carrier_name;
