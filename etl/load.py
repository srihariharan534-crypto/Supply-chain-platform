import pandas as pd
import logging
import sqlite3
from sqlalchemy import create_engine
from config.settings import settings
import os

logger = logging.getLogger(__name__)

def load_to_warehouse(df: pd.DataFrame, table_name: str, if_exists: str = 'replace'):
    """Load a dataframe into the data warehouse (SQLite via SQLAlchemy)."""
    if df.empty:
        logger.warning(f"Empty dataframe, skipping load to {table_name}")
        return
        
    logger.info(f"Loading {len(df)} records to table '{table_name}'...")
    
    try:
        engine = create_engine(settings.DATABASE_URL)
        df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)
        logger.info(f"Successfully loaded data into {table_name}")
    except Exception as e:
        logger.error(f"Error loading data to {table_name}: {e}")

def initialize_schema():
    """Run the schema and views DDL scripts to initialize the database."""
    logger.info("Initializing Data Warehouse schema...")
    
    # Only applicable for sqlite locally
    db_path = settings.DATABASE_URL.replace("sqlite:///", "")
    
    if "sqlite" in settings.DATABASE_URL:
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            schema_dir = os.path.join(settings.BASE_DIR, "schema")
            
            # Execute schema, indexes, and views
            for script_name in ["star_schema.sql", "indexes.sql", "views.sql"]:
                script_path = os.path.join(schema_dir, script_name)
                if os.path.exists(script_path):
                    with open(script_path, 'r') as f:
                        cursor.executescript(f.read())
                    logger.info(f"Executed {script_name}")
                else:
                    logger.warning(f"Script not found: {script_path}")
            
            conn.commit()
            conn.close()
            logger.info("Schema initialization complete.")
        except Exception as e:
            logger.error(f"Error initializing schema: {e}")
    else:
        logger.info("Non-SQLite database. Skipping local script execution for now.")
