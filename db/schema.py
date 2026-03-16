import sqlite3
from pathlib import Path

def create_generated_notes_table():
    db_path = Path(__file__).resolve().parents[1] / "clinical_notes.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS generated_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encounter_id TEXT NOT NULL,
            generated_note TEXT NOT NULL,
            model_name TEXT,
            generation_timestamp TEXT,
            quality_score REAL,
            FOREIGN KEY(encounter_id) REFERENCES clinical_notes_base(encounter_id)
        );
    """)

    conn.commit()
    conn.close()
    print("generated_notes table created (or already exists).")
