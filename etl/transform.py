import pandas as pd
import logging
import numpy as np

logger = logging.getLogger(__name__)

def transform_inventory(df: pd.DataFrame) -> pd.DataFrame:
    """Clean, standardize and transform inventory data."""
    if df.empty:
        return df
    
    logger.info("Transforming inventory data...")
    # Fill missing values
    df['safety_stock'] = df['safety_stock'].fillna(0)
    df['reorder_point'] = df['reorder_point'].fillna(0)
    
    # Calculate total value
    df['total_value'] = df['quantity_on_hand'] * df['unit_cost']
    
    # Standardize dates
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    
    return df

def transform_supplier(df: pd.DataFrame) -> pd.DataFrame:
    """Clean, standardize and transform supplier data."""
    if df.empty:
        return df
        
    logger.info("Transforming supplier data...")
    # Normalize text fields
    df['supplier_name'] = df['supplier_name'].str.title()
    df['country'] = df['country'].str.upper()
    
    # Handle risks
    df['risk_rating'] = df['risk_rating'].fillna('Unknown')
    
    return df

def transform_logistics(df: pd.DataFrame) -> pd.DataFrame:
    """Clean, standardize and transform logistics data."""
    if df.empty:
        return df
        
    logger.info("Transforming logistics data...")
    # Convert dates
    df['dispatch_date'] = pd.to_datetime(df['dispatch_date'])
    df['expected_arrival_date'] = pd.to_datetime(df['expected_arrival_date'])
    df['actual_arrival_date'] = pd.to_datetime(df['actual_arrival_date'])
    
    # Calculate delay
    df['delay_days'] = (df['actual_arrival_date'] - df['expected_arrival_date']).dt.days
    df['delay_days'] = df['delay_days'].apply(lambda x: max(x, 0)) # Only positive delays
    
    return df

def transform_demand(df: pd.DataFrame) -> pd.DataFrame:
    """Clean, standardize and transform demand data."""
    if df.empty:
        return df
        
    logger.info("Transforming demand data...")
    df['date'] = pd.to_datetime(df['date'])
    df['revenue'] = df['sales_quantity'] * df['revenue'] / df['sales_quantity'].replace(0, 1) # Ensure safe division
    
    return df
