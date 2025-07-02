import math

print("Investment - to calculate the aount of interest you'll earn on your investment.")
print("Bond - to calculate the aount of you'll have to pay on a home loan.")

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

if choice.lower() == "investment":
    p_deposit_amount = int(input("Enter amount of money to deposit: "))
    r_interest_rate = float(input("Enter interest as Percentage (without %, e.g. 1.4): ")) / 100 
    t_number_years = int(input("Enter number of years you plan to invest: "))

    second_choice = input("Compound or Simple: ").lower()  
    if second_choice == "simple":
        A = p_deposit_amount * (1 + r_interest_rate * t_number_years)
        print("Total amount with simple interest:", A)

    elif second_choice == "compound":
        B = p_deposit_amount * (1 + r_interest_rate) ** t_number_years
        print("Total amount with compound interest:", B)

    else:
        print("Invalid choice! Please enter 'simple' or 'compound'.")

elif choice.lower() == "bond":
    house_value = int(input("Enter present value of the house? "))
    interest_rate = int(input("Enter interest rate? "))
    number_months = int(input("Enter number of months they plant to take to repay the bond, e.g 48"))

    # repayment =   (i * P)                   /            (1 - (1 + i) ** (-n))
    repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-number_months))

    print(repayment)


# 2. At the top of the file include the line: import math 
import math

# 3. Write the code that will do the following:

# ● The first output that the user sees when the program runs should look like this: 
# Investment - to calculate the amount of interest you'll earn on your investment. 
# Bond - to calculate the amount you'll have to pay on a home loan. 
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

# ● Enter either “investment” or “bond” from the menu above to proceed:
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# ● How the user capitalises their selection should not affect how the program proceeds. 
# In other words, “Bond”, “bond”, “BOND”, should all be recognised as valid entries.
# (Handled using .lower() above)

# ● If the user selects “Investment”, “investment”, “INVESTMENT”, ask the user to input:
if choice.lower() == "investment":
    # ○ The amount of money that they are depositing.
    p_deposit_amount = float(input("Enter amount of money to deposit: "))

    # ○ The interest rate (as a percentage). Only the number of the interest rate should be entered 
    # – don’t worry about having to deal with the added “%”, e.g., the user should enter 8 and not 8%.
    r_interest_rate = float(input("Enter interest rate (as percentage, e.g. 8 not 8%): ")) / 100

    # ○ The number of years they plan on investing.
    t_number_years = int(input("Enter number of years you plan to invest: "))

    # ○ Then ask the user to input if they want “simple” or “compound” interest, and store this in a variable called interest.
    interest = input("Enter 'simple' or 'compound' interest: ").lower()

    # Depending on whether or not they typed “simple” or “compound”, output the appropriate amount that they will get back 
    # after the given period at the specified interest rate.

    # If simple interest:
    if interest == "simple":
        # The total amount when simple interest is applied is calculated as follows: A = P * (1 + r*t)
        A = p_deposit_amount * (1 + r_interest_rate * t_number_years)
        print(f"Total amount with simple interest: {round(A, 2)}")

    # If compound interest:
    # The total amount when compound interest is applied is calculated as follows: A = P * math.pow((1+r),t)
    elif interest == "compound":
        A = p_deposit_amount * math.pow((1 + r_interest_rate), t_number_years)
        print(f"Total amount with compound interest: {round(A, 2)}")

    else:
        # ● If the user doesn’t type in a valid input, show error message.
        print("Invalid choice! Please enter 'simple' or 'compound'.")

# ● If the user selects “bond”, ask the user to input:
elif choice.lower() == "bond":
    # ○ The present value of the house. e.g., 100 000.
    p_house_value = float(input("Enter the present value of the house: e.g., 100 000."))

    # ○ The interest rate.
    annual_interest_rate = float(input("Enter annual interest rate (as percentage, e.g. 7 not 7%): "))

    # ○ The number of months they plan to take to repay the bond.
    n_number_months = int(input("Enter the number of months you plan to repay the bond (e.g. 120): "))

    # Repayment formula:
    # The monthly interest rate is the annual interest rate divided by 12.
    i_monthly_interest_rate = (annual_interest_rate / 100) / 12

    # repayment = (i * P) / (1 - (1 + i)**(-n))
    repayment = (i_monthly_interest_rate * p_house_value) / (1 - math.pow((1 + i_monthly_interest_rate), - n_number_months))

    print(f"Monthly repayment amount: {round(repayment, 2)}")

# ● If the user doesn’t type in a valid input, show error message.
else:
    print("Invalid selection. Please enter 'investment' or 'bond'.")
