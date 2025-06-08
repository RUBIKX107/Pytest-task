import pandas as pd
from pipeline import load_data, clean_data, add_age_group

def test_load_data():
    df = load_data()
    assert not df.empty
    assert 'name' in df.columns
    assert 'age' in df.columns

def test_clean_data():
    df = load_data()
    cleaned_df = clean_data(df)
    assert cleaned_df.isnull().sum().sum() == 0
    assert len(cleaned_df) < len(df)  # because we removed some rows

def test_add_age_group():
    df = pd.DataFrame({'age': [25, 35]})
    df = add_age_group(df)
    assert 'age_group' in df.columns
    assert df['age_group'].tolist() == ['young', 'adult']
