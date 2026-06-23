import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def create_logistics_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate logistics features.
    """
    if df.empty: return df
    
    # Feature Creation
    df['is_delayed'] = (df['delay_days'] > 0).astype(int)
    df['cost_per_day'] = df['transport_cost'] / (df['delay_days'] + 5) # +5 for base transit
    
    # Encoding Categorical Variables
    le = LabelEncoder()
    if 'carrier_name' in df.columns:
        df['carrier_encoded'] = le.fit_transform(df['carrier_name'])
        
    if 'status' in df.columns:
        df['status_encoded'] = le.fit_transform(df['status'])
    
    # Scaling numerical features
    scaler = StandardScaler()
    scaled_cols = ['transport_cost', 'delay_days', 'cost_per_day']
    if all(col in df.columns for col in scaled_cols):
        df[[f"{col}_scaled" for col in scaled_cols]] = scaler.fit_transform(df[scaled_cols])
        
    return df
