import pandas as pd

filepath="InventoryManagement/inventory1.csv"
df = pd.read_csv(filepath)
df["Date of expiry"] = pd.to_datetime(df["Date of expiry"])