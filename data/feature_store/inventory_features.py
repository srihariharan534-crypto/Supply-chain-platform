import pandas as pd
from sklearn.preprocessing import StandardScaler

def create_inventory_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate inventory features.
    """
    if df.empty: return df
    
    # Feature Creation: Run rate and Days of Supply
    # Assuming average daily demand of 50 for placeholder, ideally joined from demand table
    df['avg_daily_demand'] = 50 
    df['days_of_supply'] = df['quantity_on_hand'] / df['avg_daily_demand'].replace(0, 1)
    
    # Aggregations
    df['is_stockout_risk'] = (df['quantity_on_hand'] <= df['reorder_point']).astype(int)
    df['is_overstocked'] = (df['quantity_on_hand'] > (df['safety_stock'] * 3)).astype(int)
    
    # Scaling numerical features
    scaler = StandardScaler()
    scaled_cols = ['quantity_on_hand', 'total_value', 'days_of_supply']
    if all(col in df.columns for col in scaled_cols):
        df[[f"{col}_scaled" for col in scaled_cols]] = scaler.fit_transform(df[scaled_cols])
        
    return df
