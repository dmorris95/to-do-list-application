#declare task list and status list
task_list = []
status_list = []

#filling out menu function
def menu_ai():
    user_choice, menu_choice = 0, 0
    menu_list = ["1. Add a task", "2. View tasks", "3. Mark a task as complete", "4. Delete a task", "5. Quit"]
    
    #show start menu and await user choice
    print("Welcome to the To-Do List App!")
    try:
        while menu_choice != 5:
            print("Menu:")
            for i in menu_list:
                print(i)
            menu_choice = menu_input()
    except:
        print("An unforeseen error occured! Please try again!")
    finally:
        print("Thank you for using the To-Do List application!")
#function that takes the users input and check for valid input
def menu_input():
    try:
        user_choice = int(input("Please type the number of the option you wish to select: "))
        if user_choice > 0 and user_choice < 6:
            #run function based on chosen number
            if user_choice == 1:
                #run loop to ensure user does not enter a blank title
                task = ""
                while task.strip() == "":
                    task = input("Enter the task you would like to add to the list: ")
                add_task(task)
            if user_choice == 2:
                #call task list with status
                if len(task_list) == 0:
                    print("You have to enter at least 1 task first!")
                else:
                    display_list()
            if user_choice == 3:
                #call function so user can mark a task as complete
                if len(task_list) == 0:
                    print("You have to enter at least 1 task first!")
                else:
                    mark_task()
            if user_choice == 4:
                #call function to delete a task
                if len(task_list) == 0:
                    print("You must add at least 1 task first!")
                else:
                    delete_task()
        else:
            raise ValueError()        
    except ValueError:
        print("You must choose a number between 1 and 5")
    except:
        print("An unexpected error occured, please try again.")
    else: #run this as long as no input errors occured
        return user_choice

#add task by title function
def add_task(title, status = "Incomplete"):
    task_list.append(title)
    status_list.append(status)

#display task list
def display_list():
    print("Your current tasks and the status are: ")
    counter = 1
    for t in task_list:
        print(f"{str(counter)}. {t} ------- {status_list[counter-1]}")
        counter += 1

#take user input to determine which task they would like to update
def mark_task():
    #print list of the tasks
    counter = 1
    for t in task_list:
        print(f"{counter}. {t}")
        counter += 1
    
    # gather input from the user based on which task they would like change the status of
    try:
        choosen_task = int(input("Type the number of the task you would like to change or enter 0 to cancel: "))
        while choosen_task > len(task_list) or choosen_task < 0:
            choosen_task = int(input(f"You must enter a positive number and a number less than or equal to {len(task_list)}: "))
    except ValueError:
        print("Sorry but you must enter a number from the list of tasks.")
    else:
        if choosen_task == 0:
            print("Going back to Menu...")
        else:
            #take the users input and change the status in the status list
            if (status_list[choosen_task-1] == "Complete"):
                print("This task has already been completed!")
            else:
                status_list[choosen_task-1] = "Complete"

#delete an existing task from the list
def delete_task():
    #print list of tasks
    counter = 1
    for t in task_list:
        print(f"{counter}. {t}")
        counter += 1
    try:
        task_picked = int(input("Type the number of the task you would like to remove, or type 0 to cancel: "))
        while task_picked > len(task_list) or task_picked < 0:
            task_picked = int(input(f"You must enter a positive number and a number less than or equal to {len(task_list)}: "))
    except ValueError:
        print("A number must be entered.")
    else:
        if task_picked == 0:
            print("Returning to menu...")
        else:
            #remove the task and its status from the list
            task_list.pop(task_picked-1)
            status_list.pop(task_picked-1)

menu_ai()