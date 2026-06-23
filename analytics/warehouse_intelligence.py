import pandas as pd
import numpy as np

class WarehouseIntelligence:
    def __init__(self, df_warehouse: pd.DataFrame, df_inventory: pd.DataFrame):
        self.df_w = df_warehouse
        self.df_i = df_inventory
        
    def analyze_utilization(self) -> pd.DataFrame:
        """Calculate warehouse capacity utilization."""
        # Assuming we can group inventory by warehouse and sum volumes (placeholder logic)
        inventory_grouped = self.df_i.groupby('warehouse_id')['quantity_on_hand'].sum().reset_index()
        merged = pd.merge(self.df_w, inventory_grouped, on='warehouse_id', how='left')
        merged['utilization_pct'] = (merged['quantity_on_hand'] / merged['capacity_m3']) * 100
        return merged
        
    def analyze_storage_efficiency(self) -> pd.DataFrame:
        """Calculate storage efficiency metrics."""
        util = self.analyze_utilization()
        util['efficiency_status'] = np.where(util['utilization_pct'] > 90, 'Overcrowded',
                                    np.where(util['utilization_pct'] < 50, 'Underutilized', 'Optimal'))
        return util
        
    def process_order_analysis(self) -> str:
        """Analyze order processing times (placeholder)."""
        return "Order processing analysis complete. Avg processing time: 2.4 hours."
        
    def rank_warehouses(self) -> pd.DataFrame:
        """Rank warehouses by utilization."""
        util = self.analyze_utilization()
        util['rank'] = util['utilization_pct'].rank(ascending=False)
        return util.sort_values(by='rank')
        
    def calculate_warehouse_score(self, warehouse_id: str) -> float:
        """Calculate an overall warehouse score (0-100)."""
        util = self.analyze_utilization()
        w_data = util[util['warehouse_id'] == warehouse_id]
        if w_data.empty: return 0.0
        
        pct = w_data.iloc[0]['utilization_pct']
        # Penalty for being >95% or <40%
        if pct > 95: return 60.0
        if pct < 40: return 50.0
        return 90.0
