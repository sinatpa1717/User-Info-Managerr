# path pathlib  remove
from pathlib import Path

def remove_user():
    masir = Path("data")
    sarch_user_remove = input("Remove user: ".title())
    path_file = masir / f"{sarch_user_remove}.json"
    
    if path_file.exists():
        path_file.unlink()
        massage = "✅"
        print(massage)
    else :
        massage1 = "❌"
        print(massage1)
    
