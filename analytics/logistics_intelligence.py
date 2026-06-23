import pandas as pd
import numpy as np

class LogisticsIntelligence:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def analyze_route_efficiency(self) -> pd.DataFrame:
        """Calculate route efficiency based on transport cost and delays."""
        # Efficiency is inversely proportional to cost and delay
        self.df['route_efficiency_index'] = 10000 / (self.df['transport_cost'] * (self.df['delay_days'] + 1))
        return self.df
        
    def perform_delivery_analysis(self) -> dict:
        """Analyze overall delivery performance."""
        total = len(self.df)
        delayed = len(self.df[self.df['status'] == 'Delayed'])
        on_time = total - delayed
        return {
            "on_time_rate": on_time / total if total > 0 else 0,
            "delayed_rate": delayed / total if total > 0 else 0,
            "avg_delay_days": self.df['delay_days'].mean()
        }
        
    def analyze_transportation_cost(self) -> float:
        """Calculate total and average transportation costs."""
        return self.df['transport_cost'].mean()
        
    def shipment_tracking_summary(self) -> pd.DataFrame:
        """Summarize shipments by status."""
        return self.df.groupby('status').size().reset_index(name='count')
        
    def calculate_logistics_score(self) -> float:
        """Calculate an overall logistics score (0-100)."""
        delivery_stats = self.perform_delivery_analysis()
        on_time_score = delivery_stats['on_time_rate'] * 100
        # Deduct points for high average delays
        delay_penalty = min(delivery_stats['avg_delay_days'] * 2, 20)
        score = max(0, min(100, on_time_score - delay_penalty))
        return score
