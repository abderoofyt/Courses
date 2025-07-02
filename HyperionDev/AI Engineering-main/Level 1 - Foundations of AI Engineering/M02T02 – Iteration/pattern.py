# arrow_size = int(input("Enter the size of the Arrow? "))
arrow_size = 5

arrow_string = arrow_string2 = ""

for counter in range(1, arrow_size):
    # Drawing each step of the arrow, both sides simultaneously
    first_arrow = "*" * counter
    last_arrow = "*" * counter

    # For the last iteration, not adding a newline to keep the arrows together
    if counter == arrow_size - 1:
        arrow_string += first_arrow  
        arrow_string2 = last_arrow + "\n" + arrow_string2
    else:
        # Adding newline for each iteration
        arrow_string += first_arrow + "\n"
        arrow_string2 = last_arrow + "\n" + arrow_string2

# Print the arrow, first, middle, and last
print(arrow_string)
print("*" * arrow_size)
print(arrow_string2)
