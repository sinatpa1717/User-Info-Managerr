# sina developer , programing python 
# path pathlib json

import json
from pathlib import Path
from def1 import function1
from def2 import show_user_list
from def3 import user_search
from def4 import remove_user
class User:
    def __init__(self , name , age , city):
        self.name = name 
        self.age = age
        self.city = city
        

class Create_user (User):
    def __init__(self, name, age, city):
        super().__init__(name, age, city)
    
    def user_file_account (self):
        """create account user , file"""
        flag = True
        while flag:
            try :
                massage = "※------※---welcome to terminal---※--------※\n"
                print(massage.upper())  
                massage1 = "create user [1]"
                print(massage1.title())
                massage2 = "show list user [2]"
                print(massage2.title())
                massage3 = "search user [3]"
                print(massage3.title())
                massage4 = "remove user [4]"
                print(massage4.title())
                massage5 = "esc terminal [q]"
                print(massage5.title())
                
                massage_user_input = input("to choose :   ")
                print(massage_user_input.title())
                
                if massage_user_input == "1":
                    function1()
                elif massage_user_input == "2":
                    show_user_list()
                elif massage_user_input == "3":
                    user_search()
                elif massage_user_input == "4":
                    remove_user()
                elif massage_user_input == "q".lower():
                    flag = False
                    break
                
            except ValueError:
                pass
            
user = User(name="",age="", city="")
x = Create_user(name="" ,city="" , age="")
x.user_file_account()