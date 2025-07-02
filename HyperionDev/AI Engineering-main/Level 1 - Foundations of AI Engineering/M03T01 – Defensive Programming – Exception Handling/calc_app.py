import os

def save_calculation(calculation):
    try:
        with open("equations.txt", "a") as file:
            file.write(calculation + "\n")
    except Exception as e:
        print(f"Error saving calculation: {e}")

def view_calculations():
    try:
        if not os.path.exists("equations.txt"):
            print("No previous calculations found.")
            return
        
        with open("equations.txt", "r") as file:
            history = file.readlines()
            if history:
                print("Previous Calculations:")
                for line in history:
                    print(line.strip())
            else:
                print("No previous calculations found.")
    except FileNotFoundError:
        print("No previous calculations found.")
    except Exception as e:
        print(f"Error reading calculations: {e}")

def calculate():
    while True:
        try:
            print("\nSimple Calculator")
            print("1. Perform a calculation")
            print("2. View previous calculations")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                try:
                    expression = input("Enter calculation (e.g., 21 + 3): ")
                    result = eval(expression)
                    calculation = f"{expression} = {result}"
                    print("Result:", result)
                    save_calculation(calculation)
                except (SyntaxError, NameError, ZeroDivisionError) as e:
                    print(f"Invalid input: {e}. Please enter a valid mathematical expression.")
                except Exception as e:
                    print(f"An error occurred: {e}")
            
            elif choice == "2":
                view_calculations()
            
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        calculate()
    except Exception as e:
        print(f"Unexpected error: {e}")