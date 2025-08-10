#developer sina python programming 
# 2025
# json pathlib for path
#python 
from pathlib import Path
import json 

#sakhte pye avalie class 
class Info:
    def __init__(self, name, age, city, language_programming):
        self.name = name 
        self.age = age 
        self.city = city
        self.language_programming = language_programming
        
    def infooo(self):
        """message user info show"""
        message = f"info user: name {self.name} , age {self.age} , city {self.city}  language programming {self.language_programming}"
        return message.title()
    #name age city programming

#sakhte akant user va file info user
class Account_user(Info):
    def __init__(self, name, age, city, language_programming):
        super().__init__(name, age, city, language_programming)
    
    def c_user(self):
        try:
            name_user = input("name user :  ".title())
            age_user = int(input("age user :   ".title()))
            city_user = input("city user :  ".title())
            lan_programming = input("language programming user :  ".title())                

            #data dic 
            user = {}
            user["name"] = name_user
            user["age"] = age_user
            user["city"] = city_user
            user["language programming"] = lan_programming

            masir = Path("kk.json")
            x = json.dumps(user, indent=4)
            tpa = masir.write_text(x)
            xxx = masir.read_text()

            print(xxx)
            print(masir.name)
            print(masir.stem)
            print(masir.suffix)
            print(masir.parent)

        except ValueError:
            pass
        
        except FileNotFoundError:
            pass


userr = Info(name="", age="", city="", language_programming="")
userr.infooo()
xuser = Account_user(name="", age="", language_programming="", city="")
xuser.c_user()
