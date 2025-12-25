import pandas as pd

file_path = pd.read_csv(r"C:\Users\DELL\Desktop\etl_pipeline\data\clinical_trials.csv")

def transforming_data(df):
   
    
    df = df.drop_duplicates()
    
    df = df.dropna(subset = ["trial_id","patient_id","drug_name","phase","start_date","end_date","outcome","adverse_events","dosage_mg","compliance_pct"])
    df["age"] = df["age"].fillna("unknown")
    df["gender"] = df["gender"].fillna("unknown")
    df["trial_site"] = df["trial_site"].fillna("unknown")
    
    df["drug_name"] = df["drug_name"].str.strip().str.title()
    df["trial_site"] = df["trial_site"].str.strip().str.title()
    df["outcome"] = df["outcome"].str.strip().str.title()
    
    
    df["start_date"] = pd.to_datetime(df["start_date"])
    df["end_date"] = pd.to_datetime(df["end_date"])
    
    df["trail_duration_days"] = df["end_date"] - df["start_date"]
    

transforming_data(file_path)
    
    