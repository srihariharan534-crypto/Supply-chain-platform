import shap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ModelExplainability:
    def __init__(self, model):
        self.model = model
        
    def generate_shap_values(self, X: pd.DataFrame):
        """Generate SHAP values for the given features."""
        # TreeExplainer is used for tree-based models like Random Forest / XGBoost
        explainer = shap.TreeExplainer(self.model)
        shap_values = explainer.shap_values(X)
        return explainer, shap_values
        
    def plot_feature_importance(self, X: pd.DataFrame, feature_names=None):
        """Plot standard tree-based feature importance."""
        if hasattr(self.model, "feature_importances_"):
            importances = self.model.feature_importances_
            if feature_names is None:
                feature_names = X.columns
                
            indices = np.argsort(importances)[::-1]
            plt.figure(figsize=(10, 6))
            plt.title("Feature Importances")
            plt.bar(range(X.shape[1]), importances[indices], align="center")
            plt.xticks(range(X.shape[1]), [feature_names[i] for i in indices], rotation=90)
            plt.tight_layout()
            # plt.show() # In a real system, this would be saved to a buffer
            return plt.gcf()
        return None
        
    def plot_shap_summary(self, explainer, shap_values, X: pd.DataFrame):
        """Generate a SHAP summary plot."""
        shap.summary_plot(shap_values, X, plot_type="bar", show=False)
        return plt.gcf()
