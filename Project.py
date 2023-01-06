from projectFunctions import *


def projects(id):
    while True:
        choice = int(input("[1] for create project\n[2] for edit project\n[3] for delete project\n[4] for view project\n[5] for exit\n---> "))
        try:
            choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5
        except:
            print("invalid choics\n")
        else:
            if choice == 1:
                try:
                    createproject(id)
                except:
                     print("\nsomething went wrong when creating\n\n")
            elif choice == 2:
                try:
                    edit = editproject(id)
                except:
                    print("\nThere is no projects to edit\n")
                else:
                    with open("projects.txt", 'w') as projectsfile:
                        projectsfile.writelines(edit)
            elif choice == 3:
                try:
                    delete = deleteproject(id)
                except:
                    print("\nThere is no projects to delete\n")
                else:
                    with open("projects.txt", 'w') as projectsfile:
                        projectsfile.writelines(delete)
            elif choice == 4:
                print("\nViewing Projects:")
                try:
                    viewproject()
                except:
                    print("\nThere is no projects to view\n")
            elif choice == 5:
                print("Thanks,see you soon :D\n")
                break
            else:
                print("\ninvalid choice\n")
   
