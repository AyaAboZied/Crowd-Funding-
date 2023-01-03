import re
from projects import projects



def namevalidation():
    name = input("enter your full name : ").strip().lower()
    while True:
        if name.isalpha() and name !="":
            break
        else:
            print("enter your name without spaces or digits")
            name = input("enter your name : ").strip().lower()
    return name



def emailvalidation():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
    email = input("enter your email : ").strip().lower()
    while True:
        if(re.fullmatch(regex, email)) and email!='':
            break
        else:
            print("Invalid Email")
            email = input( "enter valid email contains @ and .com : ").strip().lower()
    return email



def passwordvalidation():
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$'
    password = input("enter your password : ").strip()
    while True:
        if re.fullmatch(regex, password) and password!='':
            confirmedpassword = input("confirm your password : ").strip()
            if password != confirmedpassword:
                print("please confirm  your password , they are not the same")
            else:
                break
        else:
            print("enter valid password contains lowercase , uppercase ,")
            password = input("number ,special character and at least 8 character : ").strip()
    return password



def phonevalidation():
    phone = input("please enter your number : ").strip().lower()
    while True:
        if len(phone) == 11 and phone.isnumeric() and phone[0]=='0' and phone[1]=='1':
            break
        else:
            print("please enter a valid egyptian number")
            phone = input("please enter your number : ").strip().lower()
    return phone


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