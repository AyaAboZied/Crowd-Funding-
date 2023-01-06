import datetime


def namevalidation(projectname):
    while True:
        if projectname.isalpha() and projectname != "":
            break
        else:
            print("Enter your project name without spaces or digits")
            projectname = input("Project name : ").strip().lower()
    return projectname


def descvalidation(projectdescription):
    while True:
        if projectdescription.isalpha():
            break
        elif projectdescription == "":
            print("cannot be empty")
            projectdescription = input(
                "enter project decription : ").strip().lower()
        else:
            print("enter project decription without symbols or number , just use ','")
            projectdescription = input("Project decription : ").strip().lower()
    return projectdescription


def targetvalidation(target):
    while True:
        if target.isnumeric() and int(target) >= 2000 and target != "":
            break
        else:
            print("Please enter target number equal or above 2000")
            target = input("Your total target : ")
    return int(target)

# function for project date validation


def datevalidation(input_date):
    while True:
        try:
            dateobj = datetime.datetime.strptime(input_date, '%Y-%m-%d').date()
            return dateobj
        except:
            print("Incorrect data format, should be YYYY-MM-DD")
            input_date = input("Enter date in YYYY-MM-DD : ")


def periodValidation(start, end):
    while True:
        if start < end:
            break
        else:
            print("your end date can't be before the project even start")
            enddate = input("Enter end date in YYYY-MM-DD : ")
            end = datevalidation(enddate)
    return end


def fieldvalidation(id, line):
    editline = []
    fields = ["n", "d", "t", "s", "e"]
    print(
        "Enter the field name to be edited from\n[n] for name\n[d] for description\n[t] for target\n[s] for start date\n[e] for end date")
    editfield = input("---> ").strip().lower()
    if editfield in fields:
        if editfield == "n":
            projectname = input("New project name : ").strip().lower()
            line[1] = namevalidation(projectname)
        elif editfield == "d":
            projectdesc = input("New project description : ").strip().lower()
            line[2] = descvalidation(projectdesc)
        elif editfield == "t":
            target = input("New total target : ")
            line[3] = str(targetvalidation(target))
        elif editfield == "s":
            start = input("New start date in YYYY-MM-DD : ")
            line[4] = datevalidation(start)
        elif editfield == "e":
            end = input("New end date in YYYY-MM-DD: ")
            line[5] = datevalidation(end)
            end = periodValidation(line[4], line[5])
        editline.append(line)
        print("Field has been updated")
        print('\n-------------------------------------------------\n')
        return editline[0]
    else:
        print("no available field")
