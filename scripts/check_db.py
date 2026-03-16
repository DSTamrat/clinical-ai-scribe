import sys
from pathlib import Path

# Add project root to Python path
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from etl.load import get_engine
import pandas as pd

engine = get_engine()
df = pd.read_sql("SELECT COUNT(*) AS n FROM clinical_notes_base", engine)
print(df)

