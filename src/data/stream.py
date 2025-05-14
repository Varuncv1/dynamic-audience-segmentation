import time, pandas as pd
from src.config import STREAM_BATCH_SIZE, STREAM_SLEEP_SEC, PROCESSED_DATA_PATH

def stream_batches():
    df = pd.read_csv(PROCESSED_DATA_PATH)
    for i in range(0, len(df), STREAM_BATCH_SIZE):
        yield df.iloc[i:i+STREAM_BATCH_SIZE].to_dict(orient="records")
        time.sleep(STREAM_SLEEP_SEC)
