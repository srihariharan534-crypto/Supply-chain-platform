# Supply-chain-platform
## 🏗️ Architecture Diagram

```text
                    ┌─────────────────────┐
                    │   Raw Data Sources  │
                    │ Orders, Inventory   │
                    │ Suppliers, Logistics│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    ETL Pipeline     │
                    │ Extract Transform   │
                    │ Validate & Load     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Data Warehouse    │
                    │ Star Schema (SQL)   │
                    └──────────┬──────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
         ▼                     ▼                     ▼
┌────────────────┐  ┌────────────────┐  ┌────────────────┐
│ Inventory      │  │ Supplier       │  │ Logistics      │
│ Analytics      │  │ Analytics      │  │ Analytics      │
└───────┬────────┘  └───────┬────────┘  └───────┬────────┘
        │                   │                   │
        └───────────┬───────┴───────┬───────────┘
                    ▼               ▼
           ┌────────────────────────────┐
           │ Executive KPI Engine       │
           │ Forecasting & Insights     │
           └──────────────┬─────────────┘
                          │
                          ▼
           ┌────────────────
────────────┐
           │ Streamlit / Power BI       │
           │ Dashboards & Reports       │
           └──────────────┬─────────────┘
                          │
                          ▼
           ┌────────────────────────────┐
           │ Business Decisions         │
           │ Optimization & Monitoring  │
           └────────────────────────────┘
```
