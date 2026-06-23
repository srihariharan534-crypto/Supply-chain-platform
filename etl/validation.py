import pandas as pd
import logging

logger = logging.getLogger(__name__)

def validate_inventory(df: pd.DataFrame) -> bool:
    """Validate inventory dataframe before loading."""
    if df.empty:
        return False
        
    issues = 0
    if df['quantity_on_hand'].min() < 0:
        logger.error("Validation Error: Negative inventory quantity found.")
        issues += 1
        
    if df['unit_cost'].min() < 0:
        logger.error("Validation Error: Negative unit cost found.")
        issues += 1
        
    if issues == 0:
        logger.info("Inventory validation passed.")
        return True
    return False

def validate_supplier(df: pd.DataFrame) -> bool:
    """Validate supplier dataframe before loading."""
    if df.empty:
        return False
        
    if df['supplier_id'].isnull().any():
        logger.error("Validation Error: Missing supplier IDs.")
        return False
        
    logger.info("Supplier validation passed.")
    return True

def validate_logistics(df: pd.DataFrame) -> bool:
    """Validate logistics dataframe before loading."""
    if df.empty:
        return False
        
    if df['transport_cost'].min() < 0:
        logger.error("Validation Error: Negative transport cost found.")
        return False
        
    logger.info("Logistics validation passed.")
    return True

def validate_demand(df: pd.DataFrame) -> bool:
    """Validate demand dataframe before loading."""
    if df.empty:
        return False
        
    if df['sales_quantity'].min() < 0:
        logger.error("Validation Error: Negative sales quantity found.")
        return False
        
    logger.info("Demand validation passed.")
    return True
