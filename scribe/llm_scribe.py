from db.schema import create_generated_notes_table
from scribe.llm_utils import generate_note  # your LLM call
from scribe.llm_scribe import insert_generated_note
import pandas as pd
import sqlite3
from pathlib import Path

def run_llm_scribe():
    # Ensure table exists
    create_generated_notes_table()

    # Load base encounters
    db_path = Path(__file__).resolve().parents[1] / "clinical_notes.db"
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM clinical_notes_base", conn)

    for _, row in df.iterrows():
        encounter_id = row["encounter_id"]
        text = row["note_text"]

        # Call your LLM
        generated = generate_note(text)

        # Save to DB
        insert_generated_note(
            encounter_id=encounter_id,
            note=generated,
            model_name="gpt-4",  # or whatever model you're using
            quality_score=None
        )

    print("LLM note generation complete.")
