#path pathlib
from pathlib import Path

def user_search():
    masir = Path("data")
    flag = True
    while flag:
        try:
            search_user = input("name user:    ".title())
            
        except ValueError:
            pass
        except FileNotFoundError:
            print("This is not the person ❌".title())
        except KeyboardInterrupt:
            print("[q] break?")
        if search_user == "q":
            flag = False
            break
        
        file_path = masir / f"{search_user}.json"
        
        if file_path.exists():
            print(f"This is the person ✅ ".title())
        else:
            print("This is not the person❌".title())
            
