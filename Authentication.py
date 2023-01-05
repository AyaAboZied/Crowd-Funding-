import re


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



