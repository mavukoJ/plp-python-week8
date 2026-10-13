
# Week 8 Final Project: Personal Mini-Toolkit
# This program provides three simple tools in one menu.


# Tool 1: A simple calculator for basic maths.
def simple_calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("Choose an operation: +, -, *, /")
        operation = input("Enter your operation: ").strip()

        if operation == "+":
            answer = first_number + second_number
        elif operation == "-":
            answer = first_number - second_number
        elif operation == "*":
            answer = first_number * second_number
        elif operation == "/":
            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
                return
            answer = first_number / second_number
        else:
            print("Sorry, that operation is not supported.")
            return

        print(f"The answer is: {answer}")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: A to-do list that can change as tasks are added or removed.
def todo_list():
    tasks = []

    while True:
        print("\n--- My To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task '{task}' has been added.")
            else:
                print("Please enter a task.")

        elif choice == "2":
            if tasks:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("Your to-do list is empty.")

        elif choice == "3":
            if tasks:
                task = input("Enter the task to remove: ").strip()

                if task in tasks:
                    tasks.remove(task)
                    print(f"Task '{task}' has been removed.")
                else:
                    print("That task is not on your list.")
            else:
                print("There are no tasks to remove.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Please choose a number from 1 to 4.")


# Tool 3: Checks whether a whole number is even or odd.
def even_odd_checker():
    print("\n--- Even-or-Odd Checker ---")

    try:
        number = int(input("Enter a whole number: "))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    except ValueError:
        print("Please enter a valid whole number.")


# Main menu: Keeps the program running until the user quits.
def main():
    print("Welcome to My Personal Mini-Toolkit!")

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Even-or-Odd Checker")
        print("4. Quit")

        choice = input("Please choose an option (1-4): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            even_odd_checker()
        elif choice == "4":
            print("Thank you for using my toolkit. Goodbye!")
            break
        else:
            print(f"'{choice}' is not a valid choice. Please select 1, 2, 3, or 4.")


# Start the program.
if __name__ == "__main__":
    main()
