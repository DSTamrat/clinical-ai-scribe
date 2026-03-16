import pandas as pd
from pathlib import Path

def extract_raw_data():
    raw_path = Path(__file__).resolve().parents[1] / "data" / "raw" / "large_encounters.csv"
    df = pd.read_csv(raw_path)
    return df
