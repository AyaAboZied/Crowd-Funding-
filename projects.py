import datetime

# function for project name validation

def namevalidation():
    projectname = input("enter your project name : ").strip().lower()
    while True:
        if projectname.isalpha() and projectname !="":
            break
        else:
            print("enter your project name without spaces or digits")
            projectname = input("enter your project name : ").strip().lower()
    return projectname

# function for project description validation

def descvalidation():
    projectdescription = input("enter project decription : ").strip().lower()
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

# function for project total target validation

def targetvalidation():
    while True:
        target = int(input("please enter your total target : "))
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
# function for project editing / update fields validation
def is_valid (start,end):
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
            editline.append(line)
            print("field has been updated")
            return editline[0]
        elif editfield == "d":
            line[2] = descvalidation()
            editline.append(line)
            print("field has been updated")
            return editline[0]
        elif editfield == "t":
            line[3] = str(targetvalidation())
            editline.append(line)
            print("field has been updated")
            return editline[0]
        elif editfield == "s":
            start=input("please enter start date in YYYY-MM-DD : ")
            line[4] = datevalidation(start)
            editline.append(line)
            print("field has been updated")
            return editline[0]
        elif editfield == "e":
            end=input("please enter end date in YYYY-MM-DD: ")
            line[5] = datevalidation(end)
            end=is_valid(start,end)
            editline.append(line)
            print("field has been updated")
            return editline[0]
    else:
        print("no available field")


# function creating a project

def createproject(id):

    projectname = namevalidation()

    projectdescription = descvalidation()

    target = targetvalidation()

    start=input("please enter start date in YYYY-MM-DD : ")
    projectstartDate = datevalidation(start)

    end=input("please enter end date in YYYY-MM-DD : ")
    projectendDate = datevalidation(end)

    projectendDate=is_valid(projectstartDate,projectendDate)

    print("creating project")
    print(f" project name : {projectname} \n project description : {projectdescription} \n project total target : {target} \n project start date : {projectstartDate} \n project end date : {projectendDate} ")

    with open("projects.txt", 'a') as projectsfile:
        projectsfile.writelines(
            [f"{id}:{projectname}:{projectdescription}:{target}:{projectstartDate}:{projectendDate} \n"]
        )

# function deleteing a project

def deleteproject(id):
    while True:
        projectsfile = open("projects.txt", 'r')
        restfile = ""
        projectname = input("enter your project name to be deleted : ").strip().lower()
        for line in projectsfile.readlines():
            if id in line:
                if line.split(":")[1] == projectname:
                    print("project deleted")
                else:
                    restfile += line    
            else:
                print("you don't have any projects to be deleted ")
                restfile += line    
                break
        return restfile

# function viewing projects

def viewproject():
    projectsfile = open("projects.txt", 'r')
    for line in projectsfile:
        print(line)


# function edit a project

def editproject(id):
    while True:
        projectsfile = open("projects.txt", 'r')
        restfile = ""
        projectname = input("enter your project name to be edited : ").strip().lower()
        for line in projectsfile.readlines():
            if id in line:
                if line.split(":")[1] == projectname:
                    editedline = fieldvalidation(id, line.split(":"))
                    editedline = ":".join(editedline)
                    restfile += editedline
                    print("editing file")
                else:
                    restfile += line
            else:
                print("you don't have any projects to be edited ")
                restfile += line
        return restfile

# function to handle all the above

def projects(id):
    while True:
        choice = int(input("for create projects enter 1\nfor edit projects enter 2\nfor delete projects enter 3\nfor view projects enter 4\nfor exit 5  : "))
        try:
            choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5
        except:
            print("something went wrong")
        else:
            if choice == 1:
                try:
                    createproject(id)
                except:
                    print("something went wrong")
            elif choice == 2:
                try:
                    edit = editproject(id)
                except:
                    print("something went wrong")
                else:
                    with open("projects.txt", 'w') as projectsfile:
                        projectsfile.writelines(edit)
            elif choice == 3:
                try:
                    delete = deleteproject(id)
                except:
                    print("something went wrong")
                else:
                    with open("projects.txt", 'w') as projectsfile:
                        projectsfile.writelines(delete)
            elif choice == 4:
                print("viewing projects")
                try:
                    viewproject()
                except:
                    print("something went wrong")
            elif choice == 5:
                print("Thanks,see you soon :D")
                break
            else:
                print("invalid choice")
                
