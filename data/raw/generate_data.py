import pandas as pd
import numpy as np
from faker import Faker
import os
import argparse
from datetime import datetime, timedelta

# Create absolute path based on the script location to avoid relative path issues
current_dir = os.path.dirname(os.path.abspath(__file__))

def generate_inventory_data(num_records=5000):
    np.random.seed(42)
    fake = Faker()
    
    product_ids = [f"PRD-{str(i).zfill(4)}" for i in range(1, 101)]
    warehouses = [f"WH-{str(i).zfill(2)}" for i in range(1, 6)]
    
    data = {
        "inventory_id": [f"INV-{str(i).zfill(6)}" for i in range(1, num_records + 1)],
        "product_id": np.random.choice(product_ids, num_records),
        "warehouse_id": np.random.choice(warehouses, num_records),
        "quantity_on_hand": np.random.randint(0, 1000, num_records),
        "reorder_point": np.random.randint(50, 200, num_records),
        "safety_stock": np.random.randint(20, 100, num_records),
        "last_updated": [fake.date_time_between(start_date='-30d', end_date='now').strftime('%Y-%m-%d %H:%M:%S') for _ in range(num_records)],
        "unit_cost": np.round(np.random.uniform(5.0, 150.0, num_records), 2)
    }
    
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(current_dir, "inventory.csv"), index=False)
    print(f"Generated {num_records} inventory records.")

def generate_supplier_data(num_records=200):
    np.random.seed(42)
    fake = Faker()
    
    data = {
        "supplier_id": [f"SUP-{str(i).zfill(3)}" for i in range(1, num_records + 1)],
        "supplier_name": [fake.company() for _ in range(num_records)],
        "country": [fake.country() for _ in range(num_records)],
        "risk_rating": np.random.choice(["Low", "Medium", "High"], num_records, p=[0.7, 0.2, 0.1]),
        "average_lead_time_days": np.random.randint(5, 45, num_records),
        "defect_rate": np.round(np.random.beta(1, 20, num_records), 4),
        "on_time_delivery_rate": np.round(np.random.beta(20, 2, num_records), 4)
    }
    
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(current_dir, "suppliers.csv"), index=False)
    print(f"Generated {num_records} supplier records.")

def generate_shipments_data(num_records=10000):
    np.random.seed(42)
    fake = Faker()
    
    supplier_ids = [f"SUP-{str(i).zfill(3)}" for i in range(1, 201)]
    warehouses = [f"WH-{str(i).zfill(2)}" for i in range(1, 6)]
    
    start_dates = [fake.date_time_between(start_date='-1y', end_date='now') for _ in range(num_records)]
    transit_days = np.random.randint(2, 30, num_records)
    end_dates = [start + timedelta(days=int(days)) for start, days in zip(start_dates, transit_days)]
    
    data = {
        "shipment_id": [f"SHP-{str(i).zfill(6)}" for i in range(1, num_records + 1)],
        "supplier_id": np.random.choice(supplier_ids, num_records),
        "destination_warehouse_id": np.random.choice(warehouses, num_records),
        "dispatch_date": [d.strftime('%Y-%m-%d') for d in start_dates],
        "expected_arrival_date": [d.strftime('%Y-%m-%d') for d in end_dates],
        "actual_arrival_date": [(d + timedelta(days=np.random.randint(-2, 5))).strftime('%Y-%m-%d') for d in end_dates],
        "status": np.random.choice(["Delivered", "In Transit", "Delayed"], num_records, p=[0.8, 0.15, 0.05]),
        "transport_cost": np.round(np.random.uniform(500, 5000, num_records), 2),
        "carrier_name": np.random.choice(["FedEx", "DHL", "Maersk", "UPS", "LocalTransport"], num_records)
    }
    
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(current_dir, "shipments.csv"), index=False)
    df.to_csv(os.path.join(current_dir, "logistics.csv"), index=False)
    print(f"Generated {num_records} shipments/logistics records.")

def generate_logistics_data(num_records=10000):
    generate_shipments_data(num_records)

def generate_orders_data(num_records=15000):
    np.random.seed(42)
    fake = Faker()
    
    product_ids = [f"PRD-{str(i).zfill(4)}" for i in range(1, 101)]
    
    # Generate weekly demand for 2 years
    dates = pd.date_range(start="2023-01-01", end="2024-12-31", freq="W")
    
    records = []
    for date in dates:
        for pid in product_ids:
            # Introduce some seasonality based on month
            month = date.month
            season_factor = 1.0 + 0.3 * np.sin((month - 6) * np.pi / 6) 
            base_demand = np.random.randint(10, 200)
            actual_demand = int(base_demand * season_factor * np.random.uniform(0.8, 1.2))
            
            records.append({
                "date": date.strftime('%Y-%m-%d'),
                "product_id": pid,
                "sales_quantity": actual_demand,
                "revenue": actual_demand * np.round(np.random.uniform(20.0, 200.0), 2)
            })
            
            if len(records) >= num_records:
                break
        if len(records) >= num_records:
            break
            
    df = pd.DataFrame(records)
    df.to_csv(os.path.join(current_dir, "orders.csv"), index=False)
    df.to_csv(os.path.join(current_dir, "demand.csv"), index=False)
    print(f"Generated {len(df)} orders/demand records.")

def generate_demand_data(num_records=15000):
    generate_orders_data(num_records)

def generate_warehouse_data():
    data = {
        "warehouse_id": [f"WH-{str(i).zfill(2)}" for i in range(1, 6)],
        "location": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
        "capacity": [50000, 75000, 60000, 45000, 55000],
        "current_utilization": np.random.randint(60, 95, 5),
        "operating_cost_monthly": np.round(np.random.uniform(100000, 250000, 5), 2)
    }
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(current_dir, "warehouses.csv"), index=False)
    print("Generated 5 warehouse records.")

if __name__ == "__main__":
    print("Generating synthetic datasets...")
    generate_inventory_data()
    generate_supplier_data()
    generate_logistics_data()
    generate_demand_data()
    generate_warehouse_data()
    print("Done!")
