import pandas as pd
import os
from config.settings import settings
import logging

logger = logging.getLogger(__name__)

def extract_inventory_data() -> pd.DataFrame:
    """Extract inventory data from raw sources."""
    file_path = os.path.join(settings.RAW_DATA_DIR, "inventory.csv")
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Successfully extracted {len(df)} inventory records.")
        return df
    except Exception as e:
        logger.error(f"Error extracting inventory data: {e}")
        return pd.DataFrame()

def extract_supplier_data() -> pd.DataFrame:
    """Extract supplier data from raw sources."""
    file_path = os.path.join(settings.RAW_DATA_DIR, "suppliers.csv")
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Successfully extracted {len(df)} supplier records.")
        return df
    except Exception as e:
        logger.error(f"Error extracting supplier data: {e}")
        return pd.DataFrame()

def extract_logistics_data() -> pd.DataFrame:
    """Extract logistics data from raw sources."""
    file_path = os.path.join(settings.RAW_DATA_DIR, "logistics.csv")
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Successfully extracted {len(df)} logistics records.")
        return df
    except Exception as e:
        logger.error(f"Error extracting logistics data: {e}")
        return pd.DataFrame()

def extract_demand_data() -> pd.DataFrame:
    """Extract demand data from raw sources."""
    file_path = os.path.join(settings.RAW_DATA_DIR, "demand.csv")
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Successfully extracted {len(df)} demand records.")
        return df
    except Exception as e:
        logger.error(f"Error extracting demand data: {e}")
        return pd.DataFrame()
