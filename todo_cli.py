def display_tasks(current_tasks): #Enumerates list properly, code only written once and function can be used anywhere
    print("Current list:")
    for number, task in enumerate(current_tasks, start=1):
        print(f"{number}. {task}")

tasks = []
last_deleted = []
while True:
    choice = input("Add, View, Delete, or Quit?").strip().capitalize() # Using .strip and .capitalize because users may not input menu option exactly as shown

    if choice == "Add":
        while True:
            new_task = input("Enter the task description or B to go back: ").strip().capitalize() # Using .strip and .capitalize to keep a clean uniform look in task list
            if new_task == "B":
                break
            elif new_task in tasks:
                print("That task already exists!")
            else:
                tasks.append(new_task)
                display_tasks(tasks) # Display new task list so user can confirm correct task was added
        
    elif choice == "View":
        if tasks == []:
            print("No tasks to show!")
        else:
            display_tasks(tasks)
        
    elif choice == "Delete":
        while True:
            try:
                display_tasks(tasks) # Display task list so they can double check the number of the task they want to delete and will redisplay after one is deleted so they can confirm they deleted the correct one
                confirmation = input("Enter task number to delete, U to undo last delete, or B to go back: ").capitalize() # Define confirmation so user can return to menu using "B" 
                if confirmation == "B":                                                                                    # before converting input to integer to delete task of that number
                    break
                elif confirmation == "U":
                    tasks.append(last_deleted)
                else:
                    task_index = int(confirmation) - 1 # Convert to integer to delete using .pop with number input by user, - 1 because index starts at 0
                    last_deleted = tasks[task_index] # Save this task so user can undo if needed
                    if task_index < 0:                 # Raise error if input is less than 0 so user doesn't get unexpected result
                        raise ValueError
                    task_to_delete = tasks.pop(task_index)
            except ValueError:
                print("That's not a valid number!")
            except IndexError:
                print("That task number doesn't exist!")

    elif choice == "Quit":
        break
    
    else:
        print("Invalid option!")