# Power BI Specifications

## Executive Command Center
**Goal**: High-level strategic overview of the entire supply chain.
**Data Source**: `vw_executive_kpis` (to be created), `fact_inventory`, `fact_logistics`.
**Visuals**:
- **KPI Cards**: Overall Health Score, Perfect Order Rate, Cash-to-Cash Cycle Time.
- **Line Chart**: Revenue vs Supply Chain Costs over time.
- **Map**: Global distribution of warehouses and high-risk suppliers.

## Inventory Control Tower
**Goal**: Detailed inventory metrics and stockout risks.
**Data Source**: `vw_inventory_health`, `fact_inventory`.
**Visuals**:
- **Bar Chart**: Total Inventory Value by Warehouse.
- **Donut Chart**: Stock Status (Healthy vs Reorder vs Critical).
- **Table**: Top 10 High-Risk SKUs requiring immediate attention.

## Logistics Command Center
**Goal**: Route performance and delivery analysis.
**Data Source**: `vw_logistics_efficiency`.
**Visuals**:
- **Scatter Plot**: Transport Cost vs Delay Days by Carrier.
- **Gauge**: On-Time Delivery Rate.
- **Bar Chart**: Average Delay by Route/Destination.

## Supplier 360
**Goal**: Supplier performance and risk tracking.
**Data Source**: `vw_supplier_performance`, `dim_supplier`.
**Visuals**:
- **Matrix**: Supplier Scorecard showing Defect Rate, Lead Time, and Risk Rating.
- **Column Chart**: Number of Delayed Shipments by Supplier.
- **Slicers**: Filter by Country, Risk Rating, and Category.
