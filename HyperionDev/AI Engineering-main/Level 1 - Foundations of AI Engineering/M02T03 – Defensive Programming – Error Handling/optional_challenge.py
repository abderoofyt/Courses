numbers = [10, 20, 30, 40, 50]
divisor = input("Enter a number to divide each number in the list: ")

# Runtime Error: because divisor is a string, not a number
result = []
for number in numbers:
    # result.append(number/ int(divisor)) cast divisor to number to fix
    result.append(number/divisor)

# Complication Error: doesn't check for if divisor is zero

print("Results: ", result)
