import sqlite3 as sql
from pathlib import Path 
import pandas as pd



path=Path(__file__).parent / "inventory.db"


def connection():
    con=sql.connect(path)
    csr=con.cursor()
    con.row_factory= sql.Row
    csr.execute("PRAGMA foreign_keys=ON")
    return con
def init_db():
    with connection() as con:
         con.execute("""CREATE TABLE IF NOT EXISTS Items(
         ID INTEGER PRIMARY KEY AUTOINCREMENT,
         Name TEXT NOT NULL,
         Description TEXT,
         Unit TEXT CHECK(unit IN ('g', 'kg', 'liter', 'piece')),
         Amount REAL CHECK(amount >= 0),
         EXP DATE NOT NULL);""")

def Migrate():
  init_db()
  df = pd.read_csv("InventoryManagement/inventory1.csv")
  df["Date of expiry"] = pd.to_datetime(df["Date of expiry"]).dt.date
  with connection() as con:
      for _, row in df.iterrows():
          con.execute("INSERT INTO Items (Name, Description, Unit, Amount, EXP) VALUES (?,?,?,?,?)", (row["Name"], row["Description"], row["Unit"], row["Amount"], row["Date of expiry"]))
  print(f"Migrated {len(df)} Items")
