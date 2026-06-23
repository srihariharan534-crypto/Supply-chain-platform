import pandas as pd
from etl.transform import transform_inventory, transform_logistics
from etl.validation import validate_inventory, validate_logistics

def test_transform_inventory():
    data = {'quantity_on_hand': [100, 200], 'unit_cost': [10, 20], 'safety_stock': [None, 50], 'reorder_point': [None, 100], 'last_updated': ['2023-01-01', '2023-01-02']}
    df = pd.DataFrame(data)
    transformed = transform_inventory(df)
    
    assert transformed['safety_stock'].isna().sum() == 0
    assert transformed['reorder_point'].isna().sum() == 0
    assert list(transformed['total_value']) == [1000, 4000]

def test_validate_inventory():
    # Valid
    valid_df = pd.DataFrame({'quantity_on_hand': [100], 'unit_cost': [10]})
    assert validate_inventory(valid_df) == True
    
    # Invalid (negative quantity)
    invalid_df = pd.DataFrame({'quantity_on_hand': [-5], 'unit_cost': [10]})
    assert validate_inventory(invalid_df) == False

def test_transform_logistics():
    data = {'dispatch_date': ['2023-01-01'], 'expected_arrival_date': ['2023-01-05'], 'actual_arrival_date': ['2023-01-07']}
    df = pd.DataFrame(data)
    transformed = transform_logistics(df)
    
    assert 'delay_days' in transformed.columns
    assert list(transformed['delay_days'])[0] == 2
