import pandas as pd
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

NUM_ROWS = 50000   # change to 100000 or 250000 if you want BIGGER

symptoms = [
    "cough", "fever", "headache", "fatigue", "chest pain",
    "shortness of breath", "nausea", "dizziness", "back pain",
    "abdominal pain", "sore throat", "joint pain"
]

def generate_transcript():
    symptom = random.choice(symptoms)
    return (
        f"Doctor: What brings you in today? "
        f"Patient: I've been experiencing {symptom} for the past few days. "
        f"Doctor: When did it start? Patient: About {random.randint(1,7)} days ago. "
        f"Doctor: Any other symptoms? Patient: {fake.sentence()}"
    )

def generate_dataset(n=NUM_ROWS):
    rows = []
    start_date = datetime(2024, 1, 1)

    for i in range(1, n + 1):
        timestamp = start_date + timedelta(minutes=i * 5)
        rows.append({
            "encounter_id": i,
            "doctor_id": random.randint(100, 150),
            "patient_id": random.randint(1000, 9999),
            "timestamp": timestamp.isoformat(),
            "transcript": generate_transcript()
        })

    df = pd.DataFrame(rows)
    df.to_csv("data/raw/large_encounters.csv", index=False)
    print(f"Generated {n} synthetic encounters → data/raw/large_encounters.csv")

if __name__ == "__main__":
    generate_dataset()
