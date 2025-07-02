# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

#NameError: name 'Lion' is not defined
#missing "quotes" for string
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

#missing f of f"string"
#else it prints "This is a {animal}. It is a {} and it has {animal_type} teeth"
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

#missing parenthesis
#SyntaxError: Missing parentheses in call to 'print'.
print(full_spec)

