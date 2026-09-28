from expiry import df_sorted
from functions import add_item, delete_item, modify_item

def main():
    print(df_sorted)
    ask=int(input("What would u like to Change \n 1.Add \n 2.Delete \n 3.Modify \n anything else to exit \n >>>>"))
    if ask==1:
        add_item()
    elif ask==2:
        delete_item()
    elif ask==3:
        modify_item()
    else:
        exit


if __name__=="__main__" :
    main()
