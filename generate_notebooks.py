import nbformat as nbf
import os

def create_notebook(filename, title, sections):
    nb = nbf.v4.new_notebook()
    cells = []
    
    # Title Markdown
    cells.append(nbf.v4.new_markdown_cell(f"# {title}"))
    
    # Imports
    imports_code = \"\"\"import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import warnings
warnings.filterwarnings('ignore')

# Set plotting style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Connect to database
try:
    conn = sqlite3.connect('../data/warehouse/supply_chain.db')
    print("Successfully connected to the database.")
except Exception as e:
    print(f"Error connecting to database: {e}")
\"\"\"
    cells.append(nbf.v4.new_code_cell(imports_code))
    
    for section_title, section_code in sections.items():
        cells.append(nbf.v4.new_markdown_cell(f"## {section_title}"))
        if section_code:
            cells.append(nbf.v4.new_code_cell(section_code))
        else:
            cells.append(nbf.v4.new_code_cell("# Add your code here"))
            
    nb['cells'] = cells
    
    # Make sure notebooks dir exists
    os.makedirs('notebooks', exist_ok=True)
    with open(os.path.join('notebooks', filename), 'w') as f:
        nbf.write(nb, f)
    print(f"Generated {filename}")

if __name__ == "__main__":
    # 01 Data Exploration
    create_notebook("01_data_exploration.ipynb", "Data Exploration", {
        "Data Profiling": "query = \"SELECT name FROM sqlite_master WHERE type='table';\"\ntables = pd.read_sql_query(query, conn)\ndisplay(tables)",
        "Missing Value Analysis": "# Example for missing values\n# df.isnull().sum()",
        "Distribution Analysis": "# Example distribution\n# sns.histplot(data=df, x='column_name')"
    })
    
    # 02 Inventory Analysis
    create_notebook("02_inventory_analysis.ipynb", "Inventory Analysis", {
        "Load Inventory Data": "inventory_df = pd.read_sql_query(\"SELECT * FROM fact_inventory LIMIT 100\", conn)\ndisplay(inventory_df.head())",
        "Inventory Insights": "# Group by warehouse and sum quantity\n# inventory_df.groupby('warehouse_id')['quantity_on_hand'].sum().plot(kind='bar')"
    })
    
    # 03 Supplier Analysis
    create_notebook("03_supplier_analysis.ipynb", "Supplier Analysis", {
        "Load Supplier Data": "supplier_df = pd.read_sql_query(\"SELECT * FROM dim_supplier\", conn)\ndisplay(supplier_df.head())",
        "Supplier Analysis": "# Analyze risk ratings\n# sns.countplot(data=supplier_df, x='risk_rating')"
    })
    
    # 04 Logistics Analysis
    create_notebook("04_logistics_analysis.ipynb", "Logistics Analysis", {
        "Load Logistics Data": "logistics_df = pd.read_sql_query(\"SELECT * FROM fact_logistics LIMIT 100\", conn)\ndisplay(logistics_df.head())",
        "Logistics Insights": "# Analyze delays by carrier\n# sns.boxplot(data=logistics_df, x='carrier_name', y='delay_days')"
    })
    
    # 05 Demand Analysis
    create_notebook("05_demand_analysis.ipynb", "Demand Analysis", {
        "Load Demand Data": "demand_df = pd.read_sql_query(\"SELECT * FROM fact_demand LIMIT 100\", conn)\ndisplay(demand_df.head())",
        "Demand Trends": "# Plot demand over time\n# sns.lineplot(data=demand_df, x='time_id', y='sales_quantity')"
    })
    
    # 06 Forecasting Analysis
    create_notebook("06_forecasting_analysis.ipynb", "Forecasting Analysis", {
        "Prepare Data for Forecasting": "# Aggregate demand by time\n# ts_data = demand_df.groupby('time_id')['sales_quantity'].sum()",
        "Forecast Model Evaluation": "# Evaluate models (e.g., ARIMA, Prophet)\n# from statsmodels.tsa.arima.model import ARIMA"
    })
