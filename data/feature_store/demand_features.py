import pandas as pd
from sklearn.preprocessing import StandardScaler

def create_demand_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate demand features.
    """
    if df.empty: return df
    
    # Ensure date is datetime
    if 'date_actual' in df.columns:
        date_col = 'date_actual'
    elif 'date' in df.columns:
        date_col = 'date'
    else:
        return df
        
    df[date_col] = pd.to_datetime(df[date_col])
    
    # Time-based features
    df['month'] = df[date_col].dt.month
    df['quarter'] = df[date_col].dt.quarter
    df['day_of_week'] = df[date_col].dt.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    
    # Feature Creation (Lag features usually done after sorting by date/product)
    df = df.sort_values(by=[date_col])
    df['sales_quantity_lag_1'] = df['sales_quantity'].shift(1).fillna(0)
    df['sales_quantity_lag_7'] = df['sales_quantity'].shift(7).fillna(0)
    
    # Moving Averages
    df['rolling_mean_7d'] = df['sales_quantity'].rolling(window=7, min_periods=1).mean()
    
    # Scaling
    scaler = StandardScaler()
    scaled_cols = ['sales_quantity', 'revenue', 'rolling_mean_7d']
    if all(col in df.columns for col in scaled_cols):
        df[[f"{col}_scaled" for col in scaled_cols]] = scaler.fit_transform(df[scaled_cols])
        
    return df
