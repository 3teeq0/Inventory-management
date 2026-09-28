import pandas as pd
from datetime import datetime
from file import df


today = datetime.now()  
df["days_until_expiry"] = df["Date of expiry"] - today 
df["days_until_expiry"] = df["days_until_expiry"].dt.days 

df_sorted = df.sort_values("days_until_expiry")
#print(df_sorted[["Name", "Description", "Date of expiry", "days_until_expiry"]].to_string(index=False))