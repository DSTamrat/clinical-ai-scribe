from etl.extract import extract_raw_data
from etl.transform import transform_data
from etl.load import load_to_db

def run_etl():
    df = extract_raw_data()
    df = transform_data(df)
    load_to_db(df)
    print(f"ETL complete. Loaded {len(df)} rows into clinical_notes_base.")

if __name__ == "__main__":
    run_etl()
