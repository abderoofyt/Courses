# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

#Syntax error; missing brackets for print('statement')
print("Welcome to the error program")
    
#indentation and syntax error, missing brackets
print("\n")

#IndentationError: unexpected indent

#Variables declaring the user's age, casting the str to an int, and printing the result

#NameError: name 'age_Str' is not defined
#removed 1 of the == because == is used to check a condition in a if statment, 
#but = assigns a value to the variable
age_Str = "24" 

#ValueError: invalid literal for int() with base 10: '24 years old'
#age string needs to be a integer, so you'd remove the 'years old' as 24 in years is the same. 
age = int(age_Str) 

#TypeError: can only concatenate str (not "int") to str
#print("I'm" + age + "years old.") == missing spacing: else: I'm24years old.
#using age_str which is a "string" instead of age which is an integer
#or cast age to "string" using str(age), and then print("I'm " + str(age) + " years old.")
print("I'm " + age_Str + " years old.")

# Variables declaring additional years and printing the total years of age
years_from_now = "3"

#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#cast years_from_now to an integer because can't add int with str. 
#if you convert age to str, then you'd run into an issue and get 243243243243243243243243243243243243 months old. 
total_years = age + int(years_from_now)

#no error for answer_years, because you can add a string to a string, but the right answer is total_years, 
#casted to a "string"
print("The total number of years:" + str(total_years))

# Variable to calculate the total number of months from the given number of years and printing the result

#Total years convertered to months total = total_years, each year = 12 months
#NameError: name 'total' is not defined
# add the 6 because then it adds up to 330, otherwise it adds up to 324 months.
total_months = int(total_years) * 12 + 6

#TypeError: can only concatenate str (not "int") to str
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

#HINT, 330 months is the correct answer

