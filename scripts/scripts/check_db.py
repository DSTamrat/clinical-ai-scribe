from etl.load import get_engine
import pandas as pd
engine = get_engine()
df = pd.read_sql("SELECT COUNT(*) AS n FROM clinical_notes_base", engine)
print(df)
