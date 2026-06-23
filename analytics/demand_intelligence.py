import pandas as pd
import numpy as np

class DemandIntelligence:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def analyze_patterns(self) -> pd.DataFrame:
        """Analyze demand patterns over time."""
        if 'date' in self.df.columns:
            return self.df.groupby(pd.to_datetime(self.df['date']).dt.to_period('M'))['sales_quantity'].sum().reset_index()
        return self.df
        
    def calculate_velocity(self) -> pd.DataFrame:
        """Calculate demand velocity (sales per day/week)."""
        self.df['demand_velocity'] = self.df['sales_quantity'] / 7.0 # assuming weekly data
        return self.df
        
    def perform_seasonal_analysis(self) -> pd.DataFrame:
        """Perform seasonal analysis on demand."""
        if 'month' in self.df.columns:
            return self.df.groupby('month')['sales_quantity'].mean().reset_index(name='avg_seasonal_demand')
        return pd.DataFrame()
        
    def identify_fast_moving_products(self, threshold: int = 1000) -> list:
        """Identify fast moving products."""
        product_sales = self.df.groupby('product_id')['sales_quantity'].sum()
        return product_sales[product_sales > threshold].index.tolist()
        
    def identify_slow_moving_products(self, threshold: int = 100) -> list:
        """Identify slow moving products."""
        product_sales = self.df.groupby('product_id')['sales_quantity'].sum()
        return product_sales[product_sales < threshold].index.tolist()
