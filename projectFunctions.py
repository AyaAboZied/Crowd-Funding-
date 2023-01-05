from projectValidation import *

def createproject(id):
    projectname = input("enter your project name : ").strip().lower()
    projectname = namevalidation()

    projectdescription = input("enter project decription : ").strip().lower()
    projectdescription = descvalidation()

    target = int(input("please enter your total target : "))
    target = targetvalidation()

    start=input("please enter start date in YYYY-MM-DD : ")
    projectstartDate = datevalidation(start)

    end=input("please enter end date in YYYY-MM-DD : ")
    projectendDate = datevalidation(end)

    projectendDate=periodValidation(projectstartDate,projectendDate)

    print("creating project")
    print(f" project name : {projectname} \n project description : {projectdescription} \n project total target : {target} \n project start date : {projectstartDate} \n project end date : {projectendDate} ")
    print('-------------------------------------------------')

    with open("projects.txt", 'a') as projectsfile:
        projectsfile.writelines(
            [f"{id}:{projectname}:{projectdescription}:{target}:{projectstartDate}:{projectendDate} \n"]
        )


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
                else:
                    restfile += line
            else:
                print("you don't have any projects to be edited ")
                restfile += line
        return restfile


def viewproject():
    projectsfile = open("projects.txt", 'r')
    for line in projectsfile:
        print(line)
    print('-------------------------------------------------')
    
