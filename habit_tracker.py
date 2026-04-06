# -----------------------------------------------------
# Python Development Coursework - Habit Tracker Program
# -----------------------------------------------------


habits = []

def greet_user():
    print("-" * 40)
    print("Welcome to the Habit Tracker.!!")
    print("-" * 40)
    name = input("Please 'enter your name' to start program: ")
    print(f"\nHello, {name}! Please find the main menu below.")

def show_menu():
    print("\n------- MAIN MENU -------")
    print("1. Add a new habit")
    print("2. Log daily completion")
    print("3. View all habits")
    print("4. Show progress summary")
    print("5. Save to file and Exit")
    choice = input("Choose an option (1-5): ")
    return choice

def add_habit():
    print("\n--- Add New Habit ---")
    name = input("Enter habit name: ")
    target = int(input(f"What is your weekly target for '{name}'?: "))
    
    
    new_habit = {
        "name": name,
        "target": target,
        "total": 0
    }
    
    habits.append(new_habit)
    print(f"Perfect! '{name}' has been added to your habit tracker.")

def log_completion():
    if not habits:
        print("\nYou don't have any habits yet. Please add one first.")
        return
        
    print("\n--- Log Completion ---")
    for i in range(len(habits)):
        print(f"{i + 1}. {habits[i]['name']}")
        
    pick = int(input("Enter the number of the habit you completed today: ")) - 1
    
    
    if 0 <= pick < len(habits):
        confirm = input(f"Did you complete '{habits[pick]['name']}' today? (y/n): ").lower()
        if confirm == "y":
            habits[pick]["total"] += 1
            print("Perfect! Your progress has been logged.")
        else:
            print("Not logged. Please keep trying!")
    else:
        print("Sorry, invalid habit number.")

def view_habits():
    if not habits:
        print("\nThere are no habits to display.")
        return
        
    print("\n--------- YOUR HABITS ---------")
    print("Habit Name".ljust(20) + "Weekly Target".ljust(15) + "Completed")
    print("-" * 45)
    
    
    for h in habits:
        print(h["name"].ljust(20) + str(h["target"]).ljust(15) + str(h["total"]))

def show_summary():
    if not habits:
        print("\nNo data to summarize.")
        return
        
    print("\n-------- PROGRESS SUMMARY --------")
    
    for h in habits:
        if h["target"] > 0:
            percentage = (h["total"] / h["target"]) * 100
        else:
            percentage = 0
            
        print(f"{h['name']}: {h['total']}/{h['target']} days completed ({percentage:.1f}%)")

def save_data():
    if not habits:
        print("\nNo data to save. Exiting program.")
        return
        
    filename = "habit_data_report.txt"
    
    
    with open(filename, "w") as file:
        file.write("--- HABIT TRACKER FINAL REPORT ---\n\n")
        
        for h in habits:
            if h["target"] > 0:
                percentage = (h["total"] / h["target"]) * 100
            else:
                percentage = 0
                
            file.write(f"Habit: {h['name']}\n")
            file.write(f"Target: {h['target']}\n")
            file.write(f"Total Completed: {h['total']}\n")
            file.write(f"Completion Rate: {percentage:.1f}%\n")
            file.write("-" * 30 + "\n")
            
    print(f"\nAll habits and related data have been successfully saved to '{filename}'.")
    print("Goodbye!")

# ------------------------------
# MAIN PROGRAM FLOW (While Loop)
# ------------------------------

greet_user()

while True:
    user_choice = show_menu()
    
    if user_choice == "1":
        add_habit()
    elif user_choice == "2":
        log_completion()
    elif user_choice == "3":
        view_habits()
    elif user_choice == "4":
        show_summary()
    elif user_choice == "5":
        save_data()
        break  
    else:
        print("\nSorry, invalid choice. Enter a number between 1 and 5.")
