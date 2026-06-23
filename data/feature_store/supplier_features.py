import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def create_supplier_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate supplier features.
    """
    if df.empty: return df
    
    # Feature Creation
    # Calculate an overall risk score from 1-100 based on defects and lead time
    df['risk_score_numeric'] = df['defect_rate'] * 1000 + df['average_lead_time_days']
    
    # Aggregations & Grouping
    df['is_high_risk'] = (df['risk_rating'] == 'High').astype(int)
    
    # Encoding
    le = LabelEncoder()
    if 'country' in df.columns:
        df['country_encoded'] = le.fit_transform(df['country'])
    
    # Scaling
    scaler = StandardScaler()
    scaled_cols = ['average_lead_time_days', 'defect_rate', 'risk_score_numeric']
    if all(col in df.columns for col in scaled_cols):
        df[[f"{col}_scaled" for col in scaled_cols]] = scaler.fit_transform(df[scaled_cols])
        
    return df
