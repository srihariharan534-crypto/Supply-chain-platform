import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, contamination=0.05):
        self.contamination = contamination
        
    def detect_shipment_delays(self, df: pd.DataFrame) -> pd.DataFrame:
        """Detect anomalous shipment delays using Isolation Forest."""
        if df.empty or 'delay_days' not in df.columns: return df
        
        # Prepare features
        X = df[['delay_days', 'transport_cost']].fillna(0)
        
        # Train and Predict
        clf = IsolationForest(contamination=self.contamination, random_state=42)
        df['is_anomaly_shipment'] = clf.fit_predict(X)
        
        # -1 indicates anomaly, 1 indicates normal
        df['anomaly_label'] = np.where(df['is_anomaly_shipment'] == -1, 'Anomaly', 'Normal')
        return df
        
    def detect_inventory_anomalies(self, df: pd.DataFrame) -> pd.DataFrame:
        """Detect inventory anomalies (e.g., massive spikes or drops)."""
        if df.empty or 'quantity_on_hand' not in df.columns: return df
        
        X = df[['quantity_on_hand', 'unit_cost']].fillna(0)
        clf = IsolationForest(contamination=self.contamination, random_state=42)
        df['is_anomaly_inventory'] = clf.fit_predict(X)
        df['anomaly_label'] = np.where(df['is_anomaly_inventory'] == -1, 'Anomaly', 'Normal')
        return df
        
    def detect_supplier_risks(self, df: pd.DataFrame) -> pd.DataFrame:
        """Detect anomalous supplier risk patterns."""
        if df.empty or 'defect_rate' not in df.columns: return df
        
        X = df[['defect_rate', 'average_lead_time_days']].fillna(0)
        clf = IsolationForest(contamination=self.contamination, random_state=42)
        df['is_anomaly_supplier'] = clf.fit_predict(X)
        return df
        
    def detect_warehouse_bottlenecks(self, df: pd.DataFrame) -> pd.DataFrame:
        """Detect anomalous warehouse utilization."""
        if df.empty or 'utilization_pct' not in df.columns: return df
        
        # Basic statistical threshold approach for this one
        mean = df['utilization_pct'].mean()
        std = df['utilization_pct'].std()
        df['is_bottleneck'] = np.where(df['utilization_pct'] > (mean + 2*std), 'Bottleneck', 'Normal')
        return df
