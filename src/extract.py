import pandas as pd

REQUIRED_COLUMNS = [
    "trial_id", "patient_id", "age", "gender", "drug_name", "phase", "trial_site", "start_date",
    "end_date","outcome", "adverse_events", "dosage_mg", "compliance_pct"
    
]


def extraction_of_data(file_path):
    df = pd.read_csv(file_path)
    
    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    
    
    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")
    
    return df
