from projectValidation import *

def createproject(id):
    projectname = input("Project name : ").strip().lower()
    projectname = namevalidation(projectname)

    projectdescription = input("Project decription : ").strip().lower()
    projectdescription = descvalidation(projectdescription)

    target = input("Your total target : ")
    target = targetvalidation(target)

    start=input("Enter start date in YYYY-MM-DD : ")
    projectstartDate = datevalidation(start)

    end=input("Enter end date in YYYY-MM-DD : ")
    projectendDate = datevalidation(end)

    projectendDate=periodValidation(projectstartDate,projectendDate)

    print("\ncreating project")
    print(f" project name : {projectname} \n project description : {projectdescription} \n project total target : {target} \n project start date : {projectstartDate} \n project end date : {projectendDate}")
    print('\n-------------------------------------------------\n')

    with open("projects.txt", 'a') as projectsfile:
        projectsfile.writelines(
            [f"{id}:{projectname}:{projectdescription}:{target}:{projectstartDate}:{projectendDate}\n"]
        )


def deleteproject(id):
    while True:
        projectsfile = open("projects.txt", 'r')
        restfile = ""
        projectname = input("Enter your project name to be deleted : ").strip().lower()
        flag = 0
        for line in projectsfile.readlines():
            if id in line:
                if line.split(":")[1] == projectname:
                    flag = 1
                    print("project deleted")
                    print("\n-------------------------------------------------\n")
                else:
                    restfile += line    
            else:
                restfile += line  
        if flag == 0:
            print("You don't have any project has this name to be deleted ") 
            print("\n-------------------------------------------------\n") 
        return restfile


def editproject(id):
    while True:
        projectsfile = open("projects.txt", 'r')
        restfile = ""
        projectname = input("Enter your project name to be edited : ").strip().lower()
        flag = 0
        for line in projectsfile.readlines():
            if id in line:
                if line.split(":")[1] == projectname:
                    flag = 1
                    editedline = fieldvalidation(id, line.split(":"))
                    editedline = ":".join(editedline)
                    restfile += editedline
                else:
                    restfile += line
            else:
                restfile += line
        if(flag == 0):
            print("You don't have any project has this name to be edited")
            print("\n-------------------------------------------------\n")

        return restfile


def viewproject():
    projectsfile = open("projects.txt", 'r')
    for line in projectsfile:
        line = line.split(':')
        print(f"[ Name:  {line[1]},  Description:  {line[2]},  Target:  {line[3]},  StartDate:  {line[4]},  EndDate:  {line[5].strip()} ]")
    print('-------------------------------------------------\n')
    
