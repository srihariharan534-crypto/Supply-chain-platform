import pandas as pd

class RecommendationEngine:
    def __init__(self, kpi_data: dict):
        self.kpis = kpi_data
        
    def generate_recommendations(self) -> list:
        """Generate business recommendations with explanations."""
        recommendations = []
        
        inv = self.kpis.get("inventory", {})
        if inv.get("stockout_risk_percentage", {}).get("status") == "Critical":
            recommendations.append({
                "domain": "Inventory",
                "action": "Increase Safety Stock",
                "explanation": "Stockout risk is critically high. Expedite shipments for top-selling SKUs."
            })
            
        log = self.kpis.get("logistics", {})
        if log.get("on_time_delivery_rate", {}).get("status") in ["Warning", "Critical"]:
            recommendations.append({
                "domain": "Logistics",
                "action": "Switch Carriers on High-Risk Routes",
                "explanation": "On-time delivery is suffering. Identify bottleneck carriers and reallocate volume."
            })
            
        if not recommendations:
            recommendations.append({
                "domain": "System",
                "action": "Maintain Current Operations",
                "explanation": "All major KPIs are within normal operating ranges."
            })
            
        return recommendations

class AlertEngine:
    def __init__(self, anomaly_data: pd.DataFrame):
        self.df = anomaly_data
        
    def generate_alerts(self) -> list:
        """Generate automatic alerts based on anomalies."""
        alerts = []
        if 'anomaly_label' in self.df.columns:
            anomalies = self.df[self.df['anomaly_label'] == 'Anomaly']
            for _, row in anomalies.iterrows():
                alerts.append(f"ALERT: Anomaly detected for {row.name} - immediate review required.")
        return alerts

class ExecutiveDecisionEngine:
    def __init__(self, kpis, recommendations, alerts):
        self.kpis = kpis
        self.recommendations = recommendations
        self.alerts = alerts
        
    def generate_executive_brief(self) -> dict:
        """Produce a high-level brief for executives."""
        return {
            "health_score": "85/100", # Placeholder calculated score
            "critical_alerts_count": len(self.alerts),
            "top_recommendations": self.recommendations[:3]
        }
