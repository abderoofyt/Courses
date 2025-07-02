# 1. Code a program that will read from the text fi le inventory.txt and perform the following on the data to prepare for presentation to your managers:
class Shoe:
    # 2. Inside this fi le, you will fi nd a class named Shoe with the following attributes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    # 3. Inside this class define the following methods:
    # ● get_cost – Returns the cost of the shoes.
    def get_cost(self):
        return self.cost
    
    # ● get_quantity – Returns the quantity of the shoes.
    def get_quantity(self):
        return self.quantity
    
    # ● __str__ – This method returns a string representation of a class.
    # ■ Read more about the __str__ special method if you are unsure how to implement it
    def __str__(self):
        return (f"Product: {self.product}, Code: {self.code}, Country: {self.country}, "
                f"Cost: ${self.cost:.2f}, Quantity: {self.quantity}")


# 4. Outside this class create a shoes_list variable with an empty list. This variable will be used to store a list of shoe objects.
shoe_list = []

# 5. Then you must defi ne the following functions outside the class:
# ● read_shoes_data – This function will open the fi le inventory.txt and read the data from this fi le, then create a shoe object with 
# this data and append this object to the shoe list. One line in this fi le represents data to create one object of shoes. You must use the 
# try-except blocks in this function for error handling. Remember to skip the fi rst line using your code.
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip header
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    country, code, product, cost, quantity = parts
                    shoe = Shoe(country, code, product, float(cost), int(quantity))
                    shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error: 'inventory.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# ● capture_shoes – This function will allow a user to capture data about a shoe and use this data to create a shoe object and append this object 
# inside the shoe list.
def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter shoe code: ")
    product = input("Enter product name: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    print("Shoe successfully added.")


# ● view_all – This function will iterate over the shoe list and print the details of the shoes returned from the __str__ function. 
# (Optional: you can organise your data in a table format by using Python’s tabulate module.)

def view_all():
    if not shoe_list:
        print("No shoes available.")
    for shoe in shoe_list:
        print(shoe)


# ● re_stock – This function will fi nd the shoe object with the lowest quantity, which are the shoes that need to be restocked. Ask the user if 
# they want to add this quantity of shoes and then update it. This quantity should be updated on the fi le for this shoe.
def re_stock():
    if not shoe_list:
        print("No shoes in stock.")
        return

    lowest_shoe = min(shoe_list, key=lambda s: s.get_quantity())
    print(f"The shoe with the lowest stock is:\n{lowest_shoe}")

    restock = input("Do you want to restock this item? (yes/no): ").strip().lower()
    if restock == "yes":
        try:
            additional_quantity = int(input("Enter the quantity to add: "))
            lowest_shoe.quantity += additional_quantity
            update_inventory_file()  
            print("Stock updated successfully.")
        except ValueError:
            print("Invalid input. Quantity should be a number.")


def update_inventory_file():
    try:
        with open("inventory.txt", "w") as file:
            file.write("country,code,product,cost,quantity\n") 
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        print("Inventory file updated successfully.")
    except Exception as e:
        print(f"An error occurred while updating the file: {e}")



# ● search_shoe – This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.

def search_shoe():
    code = input("Enter shoe code to search: ").strip()
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found.")


# ● value_per_item – This function will calculate the total value for each item. Please keep the formula for value in mind; value = cost * quantity. 
# Print this information on the console for all the shoes.
def value_per_item():
    for shoe in shoe_list:
        total_value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product} (Code: {shoe.code}) - Total Value: ${total_value:.2f}")


# ● highest_qty – Write code to determine the product with the highest quantity and print this shoe as being for sale.
def highest_qty():
    if not shoe_list:
        print("No shoes in stock.")
        return
    highest_shoe = max(shoe_list, key=lambda s: s.get_quantity())
    print(f"The shoe with the highest quantity for sale is:\n{highest_shoe}")


# 6. Now create a menu that executes each function above. This menu should be inside the while loop. Be creative!
def main_menu():
    read_shoes_data()

    print("\n !_Welcome to the Shoe Inventory System_! ")

    while True:
        print("\nWhat would you like to do?")
        print("1 - View all shoes")
        print("2 - Add new shoe")
        print("3 - Search for a shoe by code")
        print("4 - Restock a shoe")
        print("5 - Show total value per item")
        print("6 - Highest Quality")
        print("7 - Reload Data")
        print("0 - ❌ Exit")

        choice = input("Enter your choice (0-7): ").strip()

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            search_shoe()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            shoe_list.clear()
            read_shoes_data()
            print("Data reloaded successfully.")
        elif choice == "0":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 7.")




main_menu()
