import re

def namevalidation(name):
    while True:
        if name.isalpha() and name !="":
            break
        else:
            print("Enter your name without spaces or digits\n")
            name = input("Enter your name : ").strip().lower()
    return name



def emailvalidation(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
    while True:
        if(re.fullmatch(regex, email)) and email!='':
            break
        else:
            print("Invalid Email")
            email = input( "Enter valid email contains @ and .com : ").strip().lower()
    return email



def passwordvalidation(password):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$'
    while True:
        if re.fullmatch(regex, password) and password!='':
            confirmedpassword = input("Confirm your password : ").strip()
            if password != confirmedpassword:
                print("Please confirm  your password , they are not the same\n")
            else:
                break
        else:
            print("The password must contains lowercase , uppercase , number ,special character and at least 8 character")
            password = input("Enter your password : ").strip()
    return password



def phonevalidation(phone):
    while True:
        if len(phone) == 11 and phone.isnumeric() and phone[0]=='0' and phone[1]=='1':
            break
        else:
            print("Please enter a valid egyptian number")
            phone = input("Enter your number : ").strip().lower()
    return phone



