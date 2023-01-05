from Authentication import *
from Project import projects

def registration():
    fullname = namevalidation()
    with open("users.txt", 'a') as userfile:
        userfile.writelines([f"{id(fullname)}:{fullname}:"])

    email = emailvalidation()
    with open("users.txt", 'a') as userfile:
        userfile.write(f"{email}:")

    password = passwordvalidation()
    with open("users.txt", 'a') as userfile:
        userfile.write(f"{password}:")

    phone = phonevalidation()
    with open("users.txt", 'a') as userfile:
        userfile.write(f"{phone}\n")

    print("your registration goes successfully")
    print('-------------------------------------------------')
    choiceforlogin = input("do you want to login now?[y/n] ").strip().lower()
    print('-------------------------------------------------')

    try:
        choiceforlogin == "y" or choiceforlogin == "n"
    except:
        print("something went wrong")
    else:
        if choiceforlogin == "y":
            login()
        elif choiceforlogin == "n":
            print("Thanks,see you soon :D")
        else:
            print("invalid input")


def login():
    loginemail = input("please enter your email : ").strip().lower()
    try:
        with open("users.txt", 'r') as userfile:
            data = userfile.read()
            data = data.split(":")
    except:
        print("something went wrong")
    else:
        while True:
            if loginemail in data:
                passuser = input("please enter your password : ").strip()
                if data[data.index(loginemail)+1] == passuser:
                    print(f"welcome {data[data.index(loginemail)-1]}")
                    print('-------------------------------------------------')
                    try:
                        projects(data[data.index(loginemail)-2])
                    except:
                        print("something went wrong")
                    break
                else:
                    print("Invalid password , try again")
            else:
                print("Invalid email , try again")
                loginemail = input("please enter your email : ").strip().lower()
