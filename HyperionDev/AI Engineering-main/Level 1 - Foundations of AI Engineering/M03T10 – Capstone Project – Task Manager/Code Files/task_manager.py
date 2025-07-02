import os
from datetime import datetime

# ===== Ensure required files exist =====
def initialize_files():
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as f:
            f.write("admin, admin123\n")

    if not os.path.exists("task.txt"):
        with open("task.txt", "w") as f:
            pass

# ===== Load users into a dictionary =====
def load_users():
    users = {}
    with open("user.txt", "r") as f:
        for line in f:
            if line.strip() and len(line.strip().split(", ")) == 2:
                username, password = line.strip().split(", ")
                users[username] = password
    return users

# ===== Login Function =====
def login(users):
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            print("Login successful.")
            return username
        else:
            print("Invalid credentials. Try again.")

# ===== Register a new user =====
def register_user():
    users = load_users()  
    new_username = input("Enter new username: ")

    if new_username in users:
        print("⚠️ Username already exists. Please choose a different username.")
        return

    new_password = input("Enter new password: ")
    confirm_password = input("Confirm password: ")

    if new_password == confirm_password:
        with open("user.txt", "a") as f:
            f.write(f"\n{new_username}, {new_password}")
        print("✅ New user registered.")
    else:
        print("❌ Passwords do not match. Try again.")


# ===== Add a new task =====
def add_task():
    users = load_users()

    if not users:
        print("⚠️ No users are registered. Please register a user first.")
        register_user()
        return

    print("\nSelect a user to assign the task to:")
    user_list = list(users.keys())

    for i, user in enumerate(user_list, start=1):
        print(f"{i}. {user}")

    while True:
        try:
            choice = int(input("Enter the number of the user (or 0 to register a new user): "))
            
            if choice == 0:
                register_user()
                return  

            elif 1 <= choice <= len(user_list):
                assigned_user = user_list[choice - 1]
                break

            else:
                print("❌ Please enter a valid number from the list.")
        
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (e.g., 10 Apr 2025): ")
    date_assigned = datetime.today().strftime("%d %b %Y")
    completed = input("Has task been completed? (Y/N): ")

    with open("task.txt", "a") as f:
        f.write(f"{assigned_user}, {title}, {description}, {due_date}, {date_assigned}, {completed}\n")

    print("✅ Task added.")

# ===== View all tasks =====
def view_all_tasks():
    with open("task.txt", "r") as f:
        lines = f.readlines()

    if not lines:
        print("There are no tasks to view.")
        return

    for line in lines:
        task = line.strip().split(", ")
        print(f'''
Task:               {task[1]}
Assigned to:        {task[0]}
Date assigned:      {task[4]}
Due date:           {task[3]}
Task complete?      {task[5]}
Description:        {task[2]}
''')

# ===== View tasks assigned to the current user =====
def view_my_tasks(current_user):
    with open("task.txt", "r") as f:
        tasks = f.readlines()

    user_tasks = []
    for i, line in enumerate(tasks):
        task = line.strip().split(", ")
        if task[0] == current_user:
            user_tasks.append((i, task)) 

    if not user_tasks:
        print("📭 No tasks assigned to you.\n")
        return

    print("\n📋 Your Assigned Tasks:\n")
    for display_index, (original_index, task) in enumerate(user_tasks, 1):
        print(f'''
Task [{display_index}]
------------------------------
Task Title:         {task[1]}
Assigned to:        {task[0]}
Date Assigned:      {task[4]}
Due Date:           {task[3]}
Task Complete?      {task[5]}
Description:        {task[2]}
''')

    while True:
        try:
            choice = int(input("Enter the task number to update it, or -1 to return to the main menu: "))
            
            if choice == -1:
                print("↩️ Returning to the main menu.\n")
                break

            if 1 <= choice <= len(user_tasks):
                task_index = user_tasks[choice - 1][0]
                task_parts = tasks[task_index].strip().split(", ")

                if task_parts[5].lower() == "yes":
                    print("✅ This task is already marked as complete.")
                else:
                    mark = input("Do you want to mark this task as complete? (yes/no): ").strip().lower()
                    if mark == "yes":
                        task_parts[5] = "Yes"
                        tasks[task_index] = ", ".join(task_parts) + "\n"
                        with open("task.txt", "w") as f:
                            f.writelines(tasks)
                        print("✅ Task updated as complete.")
                break
            else:
                print("❌ Invalid task number. Try again.")
        except ValueError:
            print("❌ Please enter a valid number.")


# ===== View Completed Tasks =====
def view_completed_tasks():
    with open("task.txt", "r") as f:
        tasks = f.readlines()

    completed_tasks = [task for task in tasks if task.strip().endswith("Yes")]

    if not completed_tasks:
        print("✅ No completed tasks to display.")
        return

    print("\n📋 Completed Tasks:\n")
    for task in completed_tasks:
        task_details = task.strip().split(", ")
        print(f'''
Task:               {task_details[1]}
Assigned to:        {task_details[0]}
Date assigned:      {task_details[4]}
Due date:           {task_details[3]}
Task complete?      {task_details[5]}
Description:        {task_details[2]}
''')


# ===== Delete a task =====
def delete_task():
    with open("task.txt", "r") as f:
        tasks = f.readlines()

    if not tasks:
        print("⚠️ No tasks available to delete.")
        return

    print("\nSelect a task to delete:")
    for i, task in enumerate(tasks, start=1):
        task_details = task.strip().split(", ")
        print(f"{i}. {task_details[1]} (Assigned to {task_details[0]}, Due {task_details[3]})")

    while True:
        try:
            choice = int(input("Enter the number of the task to delete (or 0 to cancel): "))
            if choice == 0:
                print("Task deletion canceled.")
                return
            if 1 <= choice <= len(tasks):
                task_to_delete = tasks[choice - 1]
                task_details = task_to_delete.strip().split(", ")

                confirm = input(f"Are you sure you want to delete the task: '{task_details[1]}'? (y/n): ").lower()
                if confirm == 'y':
                    # Rewriting task.txt without the deleted task
                    tasks.pop(choice - 1)
                    with open("task.txt", "w") as f:
                        f.writelines(tasks)
                    print("✅ Task deleted.")
                else:
                    print("Task deletion canceled.")
                return
            else:
                print("Please enter a valid task number.")
        except ValueError:
            print("Please enter a valid number.")

def generate_task_overview():
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    today = datetime.now().date()

    if not os.path.exists("task.txt"):
        print("⚠️ No tasks found.")
        return

    with open("task.txt", "r") as f:
        for line in f:
            if line.strip():
                total_tasks += 1
                parts = line.strip().split(", ")

                if len(parts) < 6:
                    continue  

                due_date_str = parts[4]
                completed = parts[5].strip().lower()

                try:
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                except ValueError:
                    continue 

                if completed == "yes":
                    completed_tasks += 1
                else:
                    uncompleted_tasks += 1
                    if due_date < today:
                        overdue_tasks += 1

    if total_tasks == 0:
        percent_incomplete = 0
        percent_overdue = 0
    else:
        percent_incomplete = (uncompleted_tasks / total_tasks) * 100
        percent_overdue = (overdue_tasks / total_tasks) * 100

    with open("task_overview.txt", "w") as f:
        f.write(f"Task Overview Report\n")
        f.write(f"--------------------\n")
        f.write(f"Total tasks: {total_tasks}\n")
        f.write(f"Completed tasks: {completed_tasks}\n")
        f.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        f.write(f"Overdue tasks: {overdue_tasks}\n")
        f.write(f"Percentage incomplete: {percent_incomplete:.2f}%\n")
        f.write(f"Percentage overdue: {percent_overdue:.2f}%\n")

    print("📄 Task overview report generated as 'task_overview.txt'.")

def generate_user_overview():
    users = load_users()
    user_task_data = {user: {"total": 0, "completed": 0, "uncompleted": 0, "overdue": 0} for user in users}
    total_tasks = 0
    today = datetime.now().date()

    if not os.path.exists("task.txt"):
        print("⚠️ No tasks found.")
        return

    # Process each task
    with open("task.txt", "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split(", ")

                if len(parts) < 6:
                    continue  

                username = parts[0]
                due_date_str = parts[4]
                completed = parts[5].strip().lower()

                if username not in user_task_data:
                    user_task_data[username] = {"total": 0, "completed": 0, "uncompleted": 0, "overdue": 0}

                user_task_data[username]["total"] += 1
                total_tasks += 1

                try:
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                except ValueError:
                    continue 

                if completed == "yes":
                    user_task_data[username]["completed"] += 1
                else:
                    user_task_data[username]["uncompleted"] += 1
                    if due_date < today:
                        user_task_data[username]["overdue"] += 1

    # Write user overview
    with open("user_overview.txt", "w") as f:
        f.write("User Overview Report\n")
        f.write("--------------------\n")
        f.write(f"Total users: {len(users)}\n")
        f.write(f"Total tasks: {total_tasks}\n\n")

        for username, data in user_task_data.items():
            total_user_tasks = data["total"]
            completed = data["completed"]
            uncompleted = data["uncompleted"]
            overdue = data["overdue"]

            if total_tasks > 0:
                percent_of_total = (total_user_tasks / total_tasks) * 100
            else:
                percent_of_total = 0

            if total_user_tasks > 0:
                percent_completed = (completed / total_user_tasks) * 100
                percent_uncompleted = (uncompleted / total_user_tasks) * 100
                percent_overdue = (overdue / total_user_tasks) * 100
            else:
                percent_completed = percent_uncompleted = percent_overdue = 0

            f.write(f"Username: {username}\n")
            f.write(f"  Total tasks assigned: {total_user_tasks}\n")
            f.write(f"  % of total tasks assigned: {percent_of_total:.2f}%\n")
            f.write(f"  % completed: {percent_completed:.2f}%\n")
            f.write(f"  % uncompleted: {percent_uncompleted:.2f}%\n")
            f.write(f"  % overdue (and uncompleted): {percent_overdue:.2f}%\n")
            f.write("\n")

    print("📄 User overview report generated as 'user_overview.txt'.")

# ===== Main Menu Loop =====
def main():
    initialize_files()
    users = load_users()
    current_user = login(users)

    while True:
        menu = input(
            '''\nSelect one of the following options:
r  - register a user
a  - add task
va - view all tasks
vm - view my tasks
vc - view completed tasks
del - delete tasks
gr - generate reports
e  - exit
: '''
        ).lower()

        if menu == 'r':
            if current_user == 'admin':
                register_user()
            else:
                print("⛔ Only the admin can register new users.")
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all_tasks()
        elif menu == 'vm':
            view_my_tasks(current_user)
        elif menu == 'vc':
            if current_user == 'admin':
                view_completed_tasks()
            else:
                print("⛔ Only the admin can view completed tasks.")

        elif menu == 'del':
            if current_user == 'admin':
                delete_task()
            else:
                print("⛔ Only the admin can delete tasks.")
        elif menu == 'gr':
            generate_user_overview()
            generate_task_overview()

        elif menu == 'e':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# ===== Run the program =====
if __name__ == "__main__":
    main()
