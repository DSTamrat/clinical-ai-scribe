def transform_data(df):
    # Minimal transform: rename columns if needed
    df = df.rename(columns={
        "encounter_id": "encounter_id",
        "patient_id": "patient_id",
        "provider_id": "provider_id",
        "note_text": "note_text",
        "timestamp": "timestamp"
    })
    return df
