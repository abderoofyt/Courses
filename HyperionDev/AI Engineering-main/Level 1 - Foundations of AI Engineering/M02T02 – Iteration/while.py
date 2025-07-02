sum = count = 0

while True:
    number = input("Enter number (not 0 and -1 to exit): ")
    
    if number == "-1":
        break
    if number.lstrip("-").isdigit() and int(number) != 0:
        sum += int(number)
        count += 1
    else:
        print("Invalid entry!")

print("Average =", sum / count if count else "No numbers entered.")
