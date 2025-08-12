#Function 1 for python project
#path , pathlib

from pathlib import Path

def show_user_list ():
    masir = Path("data")
    for i in masir.glob("*.json"):
        print(i.name)
    
