import psycopg2
from psycopg2.extras import execute_batch
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def load_data(df):
    
    connectdb = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        port = os.getenv("DB_PORT")
        
    )
   
    cursor = connectdb.cursor()
    
    create_query = """
    CREATE TABLE IF NOT EXISTS clinical_trials (
        trial_id VARCHAR(20) PRIMARY KEY,
        patient_id VARCHAR(20) NOT NULL,
        age INT CHECK (age > 0),
        gender VARCHAR(10),
        drug_name VARCHAR(100),
        phase VARCHAR(20),
        trial_site VARCHAR(100),
        start_date DATE,
        end_date DATE,
        outcome VARCHAR(50),
        adverse_events BOOLEAN,
        dosage_mg INT,
        compliance_pct NUMERIC(5,2),
        trial_duration_days TEXT
    );
    """
    
    cursor.execute(create_query)
    
    
    insert_query = """
    INSERT INTO clinical_trials (
        trial_id, patient_id, age, gender, drug_name, phase, trial_site,  start_date,
        end_date, outcome, adverse_events, dosage_mg, compliance_pct, trial_duration_days
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (trial_id) DO NOTHING;
    """
    
    data = df.values.tolist()

    execute_batch(cursor, insert_query, data)
    
    connectdb.commit()
    cursor.close()
    connectdb.close()
    
