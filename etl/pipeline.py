import logging
import sys
import os

# Add parent directory to path so absolute imports work when run as script
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.logging import setup_logging
from etl import extract, transform, load, validation
from data.raw.generate_data import generate_inventory_data, generate_supplier_data, generate_logistics_data, generate_demand_data

# Initialize logging
logger = setup_logging()

def run_pipeline():
    """Run the complete end-to-end ETL orchestration."""
    logger.info("=== Starting ETL Pipeline Orchestration ===")
    
    # 0. Initialize Warehouse Schema
    load.initialize_schema()
    
    # 1. Generate Synthetic Data if not present (for demo purposes)
    logger.info("Ensuring synthetic data exists...")
    generate_inventory_data()
    generate_supplier_data()
    generate_logistics_data()
    generate_demand_data()
    
    # 2. Extract Data
    logger.info("=== Step 1: Extraction ===")
    df_inv = extract.extract_inventory_data()
    df_sup = extract.extract_supplier_data()
    df_log = extract.extract_logistics_data()
    df_dem = extract.extract_demand_data()
    
    # 3. Transform Data
    logger.info("=== Step 2: Transformation ===")
    df_inv_t = transform.transform_inventory(df_inv)
    df_sup_t = transform.transform_supplier(df_sup)
    df_log_t = transform.transform_logistics(df_log)
    df_dem_t = transform.transform_demand(df_dem)
    
    # 4. Validate Data
    logger.info("=== Step 3: Validation ===")
    inv_valid = validation.validate_inventory(df_inv_t)
    sup_valid = validation.validate_supplier(df_sup_t)
    log_valid = validation.validate_logistics(df_log_t)
    dem_valid = validation.validate_demand(df_dem_t)
    
    # 5. Load Data
    logger.info("=== Step 4: Loading to Data Warehouse ===")
    if inv_valid: load.load_to_warehouse(df_inv_t, "fact_inventory")
    if sup_valid: load.load_to_warehouse(df_sup_t, "dim_supplier")
    if log_valid: load.load_to_warehouse(df_log_t, "fact_logistics")
    if dem_valid: load.load_to_warehouse(df_dem_t, "fact_demand")
    
    logger.info("=== ETL Pipeline Complete ===")

if __name__ == "__main__":
    run_pipeline()
