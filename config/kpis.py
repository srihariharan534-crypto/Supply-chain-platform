"""
Configuration definition for the 35+ Business KPIs.
These thresholds and targets are used by the KPI engine and Decision support system.
"""

KPI_THRESHOLDS = {
    # Inventory KPIs
    "inventory_turnover_ratio": {"target": 6.0, "warning_below": 4.0, "critical_below": 2.0},
    "stockout_risk_percentage": {"target": 0.05, "warning_above": 0.10, "critical_above": 0.20},
    "safety_stock_levels": {"min_days_coverage": 15, "max_days_coverage": 45},
    "reorder_point_accuracy": {"target": 0.95, "warning_below": 0.90},
    "inventory_health_score": {"target": 85, "warning_below": 70, "critical_below": 50},
    
    # Logistics KPIs
    "on_time_delivery_rate": {"target": 0.98, "warning_below": 0.92, "critical_below": 0.85},
    "route_efficiency_score": {"target": 90, "warning_below": 75},
    "transportation_cost_per_unit": {"target_max": 12.50, "warning_above": 15.00},
    "average_delivery_time_days": {"target_max": 3, "warning_above": 5},
    "logistics_performance_score": {"target": 85, "warning_below": 70},

    # Supplier KPIs
    "supplier_defect_rate": {"target_max": 0.01, "warning_above": 0.03, "critical_above": 0.05},
    "supplier_lead_time_variance": {"target_max": 2.0, "warning_above": 5.0}, # in days
    "supplier_compliance_rate": {"target": 0.98, "warning_below": 0.90},
    "supplier_risk_score": {"target_max": 30, "warning_above": 60, "critical_above": 80},
    "supplier_overall_ranking": {"min_acceptable": 70},

    # Warehouse KPIs
    "warehouse_capacity_utilization": {"target": 0.85, "warning_above": 0.95, "warning_below": 0.60},
    "order_picking_accuracy": {"target": 0.995, "warning_below": 0.98},
    "dock_to_stock_cycle_time": {"target_max": 4.0, "warning_above": 8.0}, # in hours
    "warehouse_efficiency_score": {"target": 88, "warning_below": 75},

    # Executive KPIs
    "supply_chain_resilience_score": {"target": 90, "warning_below": 75},
    "perfect_order_rate": {"target": 0.95, "warning_below": 0.90},
    "cash_to_cash_cycle_time": {"target_max": 30, "warning_above": 45}, # in days
    "supply_chain_cost_percentage_sales": {"target_max": 0.10, "warning_above": 0.15},
}

def get_kpi_threshold(kpi_name: str) -> dict:
    """Retrieve thresholds for a specific KPI."""
    return KPI_THRESHOLDS.get(kpi_name, {})
