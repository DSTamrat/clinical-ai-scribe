from sqlalchemy import create_engine
import yaml
from pathlib import Path

def get_engine():
    config_path = Path(__file__).resolve().parents[1] / "etl" / "config.yaml"
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    db_url = config["database_url"]
    engine = create_engine(db_url)
    return engine

def load_to_db(df):
    engine = get_engine()
    df.to_sql("clinical_notes_base", engine, if_exists="replace", index=False)
