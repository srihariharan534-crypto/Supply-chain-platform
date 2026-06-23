import pandas as pd
import numpy as np

class ScenarioSimulator:
    def __init__(self, base_df: pd.DataFrame):
        self.df = base_df.copy()
        
    def simulate_inventory_demand_shock(self, shock_multiplier: float) -> pd.DataFrame:
        """What-if analysis: Increase demand by a multiplier and calculate impact."""
        if 'avg_daily_demand' in self.df.columns:
            simulated = self.df.copy()
            simulated['simulated_demand'] = simulated['avg_daily_demand'] * shock_multiplier
            simulated['simulated_days_supply'] = simulated['quantity_on_hand'] / simulated['simulated_demand']
            simulated['new_stockout_risk'] = np.where(simulated['quantity_on_hand'] <= simulated['simulated_demand'] * 7, 'High', 'Low')
            return simulated
        return self.df

    def simulate_logistics_disruption(self, additional_delay_days: int) -> pd.DataFrame:
        """What-if analysis: Add delay to current logistics routes."""
        if 'delay_days' in self.df.columns:
            simulated = self.df.copy()
            simulated['simulated_delay'] = simulated['delay_days'] + additional_delay_days
            return simulated
        return self.df
        
    def simulate_supplier_lead_time_change(self, lead_time_multiplier: float) -> pd.DataFrame:
        """What-if analysis: Supplier lead times increase/decrease."""
        if 'average_lead_time_days' in self.df.columns:
            simulated = self.df.copy()
            simulated['simulated_lead_time'] = simulated['average_lead_time_days'] * lead_time_multiplier
            return simulated
        return self.df
        
    def simulate_warehouse_capacity_change(self, capacity_multiplier: float) -> pd.DataFrame:
        """What-if analysis: Expand or reduce warehouse capacity."""
        if 'capacity_m3' in self.df.columns:
            simulated = self.df.copy()
            simulated['simulated_capacity'] = simulated['capacity_m3'] * capacity_multiplier
            if 'quantity_on_hand' in simulated.columns:
                simulated['simulated_utilization'] = (simulated['quantity_on_hand'] / simulated['simulated_capacity']) * 100
            return simulated
        return self.df
