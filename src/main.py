from extract import extraction_of_data
from transform import transforming_data
from load import load_data

def main():
    file_path = r"C:\Users\DELL\Desktop\etl_pipeline\data\clinical_trials.csv"

    print("Extracting of data")
    df = extraction_of_data(file_path)

    print("Transforming of data")
    df_cleaned = transforming_data(df)

    print("Loading data into PostgreSQL")
    load_data(df_cleaned)

    print("ETL Pipeline completed successfully!")

if __name__ == "__main__":
    main()
