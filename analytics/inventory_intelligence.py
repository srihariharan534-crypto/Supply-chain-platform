import pandas as pd
import numpy as np

class InventoryIntelligence:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def calculate_stockout_risk(self) -> pd.DataFrame:
        """Calculate the probability of stockout."""
        self.df['stockout_risk'] = np.where(self.df['quantity_on_hand'] <= self.df['safety_stock'], 
                                            'High', 
                                            np.where(self.df['quantity_on_hand'] <= self.df['reorder_point'], 'Medium', 'Low'))
        return self.df
        
    def calculate_inventory_turnover(self, cogs: float, average_inventory_value: float) -> float:
        """Calculate inventory turnover ratio."""
        if average_inventory_value == 0: return 0.0
        return cogs / average_inventory_value
        
    def calculate_safety_stock(self, max_daily_usage: float, max_lead_time: float, avg_daily_usage: float, avg_lead_time: float) -> float:
        """Calculate ideal safety stock."""
        return (max_daily_usage * max_lead_time) - (avg_daily_usage * avg_lead_time)
        
    def calculate_reorder_point(self, lead_time_demand: float, safety_stock: float) -> float:
        """Calculate optimal reorder point."""
        return lead_time_demand + safety_stock
        
    def generate_inventory_health_score(self) -> pd.DataFrame:
        """Generate an overall health score (0-100) for inventory items."""
        # Simple heuristic: 100 is best. Deduct points for being under safety stock or massively over reorder point.
        conditions = [
            self.df['quantity_on_hand'] <= self.df['safety_stock'],
            (self.df['quantity_on_hand'] > self.df['safety_stock']) & (self.df['quantity_on_hand'] <= self.df['reorder_point']),
            self.df['quantity_on_hand'] > self.df['reorder_point'] * 3
        ]
        choices = [20, 60, 40]
        self.df['inventory_health_score'] = np.select(conditions, choices, default=95)
        return self.df
