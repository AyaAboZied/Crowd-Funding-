from system import *

def signinup():
    print("\n----------> Welcome to Crowd Funding Project <----------")
    print("By: Aya El-Sayed\n")
    while True:
        print('-------------------------------------------------')
        try:
            choice = int(input("[1] for login \n[2] for register\n[3] for exit\n---> "))
            choice == 1 or choice == 2 or choice == 3
        except:
            print("invalid choice\n")
        else:
            if choice == 1:
                try:
                    login()
                except:
                    print("\nsomething went wrong while login\n")
            elif choice == 2:
                try:
                    registration()
                except:
                    print("\nsomething went wrong while register\n")
            elif choice == 3:
                return
            else:
                print("\ninvalid choice\n")


signinup()
