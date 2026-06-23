import pandas as pd

class SupplierIntelligence:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def generate_supplier_scorecards(self) -> pd.DataFrame:
        """Generate comprehensive supplier scorecards."""
        self.df['scorecard_grade'] = pd.cut(self.df['risk_score_numeric'] if 'risk_score_numeric' in self.df.columns else self.df['defect_rate'], 
                                            bins=4, labels=['A', 'B', 'C', 'D'])
        return self.df
        
    def perform_risk_analysis(self) -> pd.DataFrame:
        """Analyze and categorize supplier risks."""
        return self.df.groupby('risk_rating').size().reset_index(name='count')
        
    def perform_lead_time_analysis(self) -> pd.DataFrame:
        """Analyze supplier lead times."""
        return self.df.sort_values(by='average_lead_time_days', ascending=False)
        
    def rank_suppliers(self) -> pd.DataFrame:
        """Rank suppliers based on performance metrics."""
        # Lower defect rate and lower lead time is better
        self.df['performance_rank'] = self.df['defect_rate'].rank(ascending=True) + self.df['average_lead_time_days'].rank(ascending=True)
        return self.df.sort_values(by='performance_rank')
