import streamlit as st
import pandas as pd
import numpy as np
import os

# Page Configuration
st.set_page_config(
    page_title="Supply Chain Command Center",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Helpers to load data
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data", "raw")
    
    inventory_df = pd.read_csv(os.path.join(data_dir, "inventory.csv"))
    orders_df = pd.read_csv(os.path.join(data_dir, "orders.csv"))
    suppliers_df = pd.read_csv(os.path.join(data_dir, "suppliers.csv"))
    warehouses_df = pd.read_csv(os.path.join(data_dir, "warehouses.csv"))
    shipments_df = pd.read_csv(os.path.join(data_dir, "shipments.csv"))
    
    return inventory_df, orders_df, suppliers_df, warehouses_df, shipments_df

def apply_custom_css():
    st.markdown("""
        <style>
        .kpi-card {
            background-color: #1E1E1E;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #00E676;
            margin-bottom: 20px;
        }
        .kpi-title { color: #A0A0A0; font-size: 14px; text-transform: uppercase; }
        .kpi-value { color: #FFFFFF; font-size: 28px; font-weight: bold; margin-top: 10px; }
        </style>
    """, unsafe_allow_html=True)

def render_executive_dashboard(inventory_df, orders_df, suppliers_df, warehouses_df, shipments_df):
    st.title("Executive Dashboard")
    col1, col2, col3, col4 = st.columns(4)
    
    total_inventory = inventory_df['quantity_on_hand'].sum()
    avg_supplier_score = 100 - (suppliers_df['risk_rating'] == 'High').mean() * 100
    active_alerts = len(shipments_df[shipments_df['status'] == 'Delayed'])
    on_time_rate = len(shipments_df[shipments_df['status'] == 'Delivered']) / max(1, len(shipments_df)) * 100
    
    with col1:
        st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Overall Health</div><div class='kpi-value'>{avg_supplier_score:.1f} / 100</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Active Alerts</div><div class='kpi-value' style='color:#FF3D00'>{active_alerts}</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Total Inventory Units</div><div class='kpi-value'>{total_inventory:,.0f}</div></div>", unsafe_allow_html=True)
    with col4:
        st.markdown(f"<div class='kpi-card'><div class='kpi-title'>On-Time Delivery Rate</div><div class='kpi-value'>{on_time_rate:.1f}%</div></div>", unsafe_allow_html=True)
        
    st.subheader("Key Recommendations")
    st.info("Logistics: Monitor delayed shipments closely.")
    st.warning("Inventory: Check products falling below safety stock levels.")

def render_inventory_tower(inventory_df):
    st.title("📦 Inventory Control Tower")

    col1, col2, col3, col4 = st.columns(4)

    total_units = inventory_df['quantity_on_hand'].sum()
    low_stock = inventory_df[inventory_df['quantity_on_hand'] <= inventory_df['reorder_point']]
    stockout_risk = len(low_stock) / max(1, len(inventory_df)) * 100

    with col1:
        st.metric("Total Units on Hand", f"{total_units:,.0f}")

    with col2:
        st.metric("Products to Reorder", f"{len(low_stock)}")

    with col3:
        st.metric("Stockout Risk", f"{stockout_risk:.1f}%")

    with col4:
        st.metric("Total Value (Est)", f"${(inventory_df['quantity_on_hand'] * inventory_df['unit_cost']).sum():,.2f}")

    st.divider()

    st.subheader("Reorder Recommendations")

    reorder_df = low_stock[['product_id', 'warehouse_id', 'quantity_on_hand', 'reorder_point', 'safety_stock']].head(50)
    reorder_df['Action'] = np.where(reorder_df['quantity_on_hand'] <= reorder_df['safety_stock'], 'Urgent Reorder', 'Reorder')

    st.dataframe(
        reorder_df,
        use_container_width=True
    )

    if len(reorder_df) > 0:
        urgent_count = len(reorder_df[reorder_df['Action'] == 'Urgent Reorder'])
        st.warning(f"⚠️ {urgent_count} products require immediate replenishment.")
    else:
        st.success("All products are adequately stocked.")

def render_logistics_tower(shipments_df):
    st.title("🚚 Logistics Command Center")

    col1, col2, col3 = st.columns(3)

    total_shipments = len(shipments_df)
    delayed = len(shipments_df[shipments_df['status'] == 'Delayed'])
    delivered = len(shipments_df[shipments_df['status'] == 'Delivered'])
    on_time_rate = delivered / max(1, total_shipments) * 100

    with col1:
        st.metric("On-Time Delivery", f"{on_time_rate:.1f}%")

    with col2:
        st.metric("Delayed Shipments", f"{delayed}")

    with col3:
        st.metric("Total Shipments", f"{total_shipments:,.0f}")

    st.subheader("Recent Delayed Shipments")
    st.dataframe(shipments_df[shipments_df['status'] == 'Delayed'].head(20), use_container_width=True)

def render_supplier_360(suppliers_df):
    st.title("🏭 Supplier 360")
    
    col1, col2, col3 = st.columns(3)
    high_risk = len(suppliers_df[suppliers_df['risk_rating'] == 'High'])
    with col1:
        st.metric("Total Suppliers", len(suppliers_df))
    with col2:
        st.metric("High Risk Suppliers", high_risk)
    with col3:
        st.metric("Avg Lead Time", f"{suppliers_df['average_lead_time_days'].mean():.1f} days")

    st.dataframe(
        suppliers_df[['supplier_id', 'supplier_name', 'country', 'risk_rating', 'on_time_delivery_rate']],
        use_container_width=True
    )

def render_warehouse_analytics(warehouses_df):
    st.title("🏬 Warehouse Analytics")

    avg_utilization = warehouses_df['current_utilization'].mean()
    st.metric("Avg Warehouse Utilization", f"{avg_utilization:.1f}%")

    st.bar_chart(
        warehouses_df.set_index("warehouse_id")['current_utilization']
    )
    st.dataframe(warehouses_df, use_container_width=True)

def render_forecasting(orders_df):
    st.title("📈 Demand Forecasting")

    # Aggregate demand by month
    orders_df['date'] = pd.to_datetime(orders_df['date'])
    monthly_demand = orders_df.resample('M', on='date')['sales_quantity'].sum().reset_index()
    monthly_demand['Month'] = monthly_demand['date'].dt.strftime('%Y-%m')
    
    st.line_chart(
        monthly_demand.set_index("Month")['sales_quantity']
    )

def render_risk_monitoring(suppliers_df, shipments_df):
    st.title("⚠️ Risk Monitoring")

    high_risk_suppliers = suppliers_df[suppliers_df['risk_rating'] == 'High']
    delayed_shipments = shipments_df[shipments_df['status'] == 'Delayed']
    
    if len(high_risk_suppliers) > 0 or len(delayed_shipments) > 0:
        st.error(f"{len(high_risk_suppliers)} high-risk suppliers and {len(delayed_shipments)} delayed shipments detected")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("High Risk Suppliers")
            st.dataframe(high_risk_suppliers[['supplier_id', 'supplier_name', 'country', 'defect_rate']], use_container_width=True)
            
        with col2:
            st.subheader("Delayed Shipments")
            st.dataframe(delayed_shipments[['shipment_id', 'supplier_id', 'destination_warehouse_id', 'expected_arrival_date']], use_container_width=True)
    else:
        st.success("No immediate risks detected.")

def render_optimization():
    st.title("🎯 Optimization Center")
    st.success("Recommended action: Optimize warehouse utilization by redistributing inventory from WH-02 to WH-04.")

def main():
    apply_custom_css()
    
    try:
        inventory_df, orders_df, suppliers_df, warehouses_df, shipments_df = load_data()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.info("Make sure you have run the generate_data.py script.")
        return
    
    st.sidebar.title("Navigation")
    pages = {
        "Executive Dashboard": lambda: render_executive_dashboard(inventory_df, orders_df, suppliers_df, warehouses_df, shipments_df),
        "Inventory Control Tower": lambda: render_inventory_tower(inventory_df),
        "Logistics Command Center": lambda: render_logistics_tower(shipments_df),
        "Supplier 360": lambda: render_supplier_360(suppliers_df),
        "Warehouse Analytics": lambda: render_warehouse_analytics(warehouses_df),
        "Demand Forecasting": lambda: render_forecasting(orders_df),
        "Risk Monitoring": lambda: render_risk_monitoring(suppliers_df, shipments_df),
        "Optimization Center": render_optimization
    }
    
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    # Execute selected page function
    pages[selection]()

if __name__ == "__main__":
    main()