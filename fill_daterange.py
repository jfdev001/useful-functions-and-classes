import pandas as pd
import numpy as np
def fill_daterange(df: pd.Dataframe, freq: str = "D"):
  """Add empty timestamps for non-consecutive stamps.
  
  Example:
  ```
  t           data
  2023-03-24  ...
  2023-03-26  ...
       |
       |  fill_daterange
       V
  t           data
  2023-03-24  ...
  2023-03-25  nan
  2023-03-26  ...
  ```
  """
  df = df.sort_values(by=["time"])
  start_date = df["time"].iloc[0]
  stop_date = df["time"].iloc[-1]
  date_range = pd.date_range(start_date, stop_date, freq=freq)
  df = df.reindex(date_range, fill_value=np.nan)
  return df
