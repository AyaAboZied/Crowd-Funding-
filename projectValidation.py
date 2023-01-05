import datetime


def namevalidation(projectname):
    while True:
        if projectname.isalpha() and projectname !="":
            break
        else:
            print("enter your project name without spaces or digits")
            projectname = input("enter your project name : ").strip().lower()
    return projectname



def descvalidation(projectdescription):
    while True:
        if projectdescription.isalpha():
            break
        elif projectdescription == "":
            print("cannot be empty")
            projectdescription = input("enter project decription : ").strip().lower()
        else:
            print("enter project decription without symbols or number , just use ','")
            projectdescription = input("enter project decription : ").strip().lower()
    return projectdescription


def targetvalidation(target):
    while True:
        if target >= 2000 and target !="" :
            break
        else:
            print("please enter target number equal or above 2000")
            target = input("please enter your total target : ")
    return target

# function for project date validation

def datevalidation(input_date): 
    try:
        dateobj=datetime.datetime.strptime(input_date, '%Y-%m-%d')
        return dateobj
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def periodValidation (start,end):
    while True:
        if start < end:
            break
        else :
            print("your end date can't be before the project even start")
            enddate=input("please enter end date in YYYY-MM-DD : ")
            end = datevalidation(enddate)
    return end



def fieldvalidation(id, line):
    editline = []
    fields = ["n", "d","t", "s", "e"]
    editfield = input("enter the field name to be edited from [ 'n for name', 'd for description',' t for target', 's for startdate', 'e for enddate'] :").strip().lower()
    if editfield in fields:
        if editfield == "n":
            line[1] =  namevalidation()
        elif editfield == "d":
            line[2] = descvalidation()
        elif editfield == "t":
            line[3] = str(targetvalidation())
        elif editfield == "s":
            start=input("please enter start date in YYYY-MM-DD : ")
            line[4] = datevalidation(start)
        elif editfield == "e":
            end=input("please enter end date in YYYY-MM-DD: ")
            line[5] = datevalidation(end)
            end=periodValidation(line[4],line[5])
        editline.append(line)
        print("field has been updated")
        print('-------------------------------------------------')
        return editline[0]
    else:
        print("no available field")


             
