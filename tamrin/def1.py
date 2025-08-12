#Function 1 for python project
# json , path , pathlib
import json
from pathlib import Path

def function1():
    """Create_user"""
    try:
        name_user = input("name user:    ".title())
        age_user = input("age user:    ".title())
        age_user = int(age_user)
        city_user = input("city user:    ".title())
        
    except ValueError:
        print("Please enter a number".title())
    
    except TypeError:
        pass
    
    
    data_user = {}
    data_user["name"] = name_user
    data_user["age"] = age_user
    data_user["city"] = city_user
    
    masir = Path(f"data/{name_user}.json")
    x = json.dumps(data_user , indent= 4 , sort_keys= True)
    masir.write_text(x)

    massage = f"Create_user ✅ : name {name_user} | age {age_user} city {city_user}"
    print (massage.title())
    
