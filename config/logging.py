import logging
import sys
from config.settings import settings

def setup_logging():
    """
    Configure the root logger with the specified log level and format.
    """
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Convert string level to logging integer
    numeric_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    
    logging.basicConfig(
        level=numeric_level,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            # Optional: Add FileHandler here to log to a file
            # logging.FileHandler("app.log")
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized at level {settings.LOG_LEVEL}")
    
    return logger

# Global logger instance
logger = setup_logging()
