
tasks = []

while True:
print("\n   'TO  DO  LIST' ")
print("1. Add Task")
print("2. View Tasks")
print("3. Delete Task")
print("4. Edit Task")
print("5. Exit")

choice = input("select: ")

if choice == "1":
task = input("Enter task: ")
tasks.append(task)
print("added Done!")

elif choice == "2" :
    if len(tasks) == 0 :
        print("No tasks yet.")
    else :
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1) :
            print(f"{i}. {t}")

            elif choice == "3" :
            if len(tasks) == 0 :
                print("No tasks to delete.")
            else :
                for i, t in enumerate(tasks, 1) :
                    print(f"{i}. {t}")

                    num = int(input("Enter task number to delete: "))

                    if 1 <= num <= len(tasks) :
                        tasks.pop(num - 1)
                        print("Deleted done!")
                    else:
print("Wrong number!")

elif choice == "4" :
    if len(tasks) == 0 :
        print("No tasks to edit.")
    else :
        for i, t in enumerate(tasks, 1) :
            print(f"{i}. {t}")

            num = int(input("Enter task number to edit: "))

            if 1 <= num <= len(tasks) :
                new_task = input("Enter new task: ")
                tasks[num - 1] = new_task
                print("Task updated !")
            else:
print("Wrong number!")

elif choice == "5" :
    print("Task finished ")
    break

else:
print("Invalid input, try again.")


