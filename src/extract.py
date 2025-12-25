import pandas as pd

REQUIRED_COLUMNS = [
    "trial_id", "patient_id", "age", "gender", "drug_name", "phase", "trial_site", "start_date",
    "end_date","outcome", "adverse_events", "dosage_mg", "compliance_pct"
    
]


def extraction_of_data():
    df = pd.read_csv(r"C:\Users\DELL\Desktop\etl_pipeline\data\clinical_trials.csv")
    
    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    
    
    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")
    
    return df

extraction_of_data()