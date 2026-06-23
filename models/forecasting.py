import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

class Forecaster:
    def __init__(self, model_dir="model_artifacts"):
        self.model_dir = model_dir
        os.makedirs(self.model_dir, exist_ok=True)
        self.models = {}

    def train_demand_forecast(self, df: pd.DataFrame, target_col="sales_quantity"):
        """Train a basic Random Forest for demand forecasting."""
        if df.empty: return
        
        # Assume df has numerical features ready
        X = df.drop(columns=[target_col, "date", "date_actual", "product_id"], errors="ignore")
        y = df[target_col]
        
        # Very simple imputation for training
        X = X.fillna(0)
        
        # Select numeric types only
        X = X.select_dtypes(include=[np.number])

        if X.empty: return
        
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X, y)
        self.models["demand"] = model
        
        with open(os.path.join(self.model_dir, "demand_model.pkl"), "wb") as f:
            pickle.dump(model, f)
            
        print("Demand model trained and saved.")

    def forecast_demand(self, features: pd.DataFrame) -> np.ndarray:
        """Generate demand forecasts."""
        if "demand" not in self.models:
            raise ValueError("Model not trained.")
            
        X = features.select_dtypes(include=[np.number]).fillna(0)
        return self.models["demand"].predict(X)
        
    def generate_metrics(self, y_true, y_pred) -> dict:
        """Generate evaluation metrics."""
        from sklearn.metrics import mean_absolute_error, mean_squared_error
        return {
            "MAE": mean_absolute_error(y_true, y_pred),
            "RMSE": np.sqrt(mean_squared_error(y_true, y_pred))
        }

    # Similar methods would exist for Inventory, Shipment, and Supplier Lead-Time
    def train_inventory_forecast(self, df: pd.DataFrame):
        pass
        
    def train_shipment_forecast(self, df: pd.DataFrame):
        pass
        
    def train_supplier_lead_time_forecast(self, df: pd.DataFrame):
        pass
