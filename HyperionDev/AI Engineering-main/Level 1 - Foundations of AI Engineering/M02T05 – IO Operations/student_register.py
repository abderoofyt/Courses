student_IDs = []

while True:
    number_id = input("Enter number of students registered (i.e. student ID's)? ")
    if number_id.isdigit():
        #Careful for in in int(number_id) is a trap
        for i in range(int(number_id)):
            while True:
                ID_entered = input("Enter Student ID(13 digits/numbers)? ")
                if len(ID_entered) == 13: 
                    if ID_entered.isdigit():
                        student_IDs.append(ID_entered)
                        break
                else:
                    print("Incorrect ID entered!")
        break
    else:
        print("Not a valued Number! Try again.")

# for j in student_IDs:
print(student_IDs)

with open("reg_form.txt", "w") as output_file:
    # Writes 'name' followed by a newline to output file
    for i in student_IDs: 
        output_file.write(i + "\n...........................................................\n")
