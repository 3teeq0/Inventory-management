from datetime import datetime
from file import df,filepath
import pandas as pd

def add_item():
    e=0
    while True:
    
        N=input("Enter Name of item:")
        D=input("Enter description of Item:")
        U=input("enter Unit (g/kg/liter/piece):")
        A=float(input("Enter amount (in float):"))
        DOE=input("Enter Date of Expiry(YYYY-MM-DD):")
        try:
            DOE=pd.to_datetime(DOE)
            break
        except ValueError:
            e=1
            print("Invalid date use YYYY-MM-DD")
    if e==0:
        df.loc[len(df)]=[N,D,U,A,DOE]
        df.to_csv(filepath, index=False)
    print(df)


def delete_item():
    global df
    while True:
        print(df)
        x=int(input("what item to delete (type no.:): "))
        try:
            df=df.drop(x)
            df.to_csv(filepath, index=False)
            break
        except :
            print("Index unavailable")
    print(df)

  
def modify_item():
    print(df)
    y=int(input("index of item: \n"))
    x=int(input("Modify what? \n 1.Name \n 2.Unit \n 3.Amount \n 4.Date \n >>>:"))
    if x==1:
        z=input("Change Name to?:")
        df.loc[y,"Name"] = z
    elif x==2:
        z=input("Unit change?")
        df.loc[y, "Unit"]=z
    elif x==3:
        z=float(input("Amount change:"))
        df.loc[y, "Amount"]=z
    elif x==4:
        z=input("Change Date to? (YYYY-MM-DD format):")
        df.loc[y,"Date of expiry"]=pd.to_datetime(z)
    df.to_csv(filepath, index=False)
    print(pd.read_csv(filepath))
