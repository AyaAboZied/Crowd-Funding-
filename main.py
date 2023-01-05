from system import *

def signinup():
    choice = int(input("for login enter 1\nfor register enter 2 :\nfor exit enter 3 : "))
    try:
        choice == 1 or choice == 2 or choice == 3
    except:
        print("invalid choice")
    else:
        if choice == 1:
            try:
                login()
            except:
                print("something went wrong")
        elif choice == 2:
            try:
                registration()
            except:
                print("something went wrong")
        elif choice == 3:
            return
        else:
            print("invalid choice")


signinup()