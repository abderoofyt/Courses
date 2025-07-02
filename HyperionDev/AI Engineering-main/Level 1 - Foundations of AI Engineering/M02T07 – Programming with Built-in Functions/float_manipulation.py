import statistics

float_list = []

for i in range(10):
    float_input = input("Enter a float (whole number/decimal): ")
    float_list.append(float(float_input))

# Calculate Total
total_num = sum(float_list)

# Calculate Mean (Average)
average = statistics.mean(float_list)

# Find min and Max

# min_value = min(float_list)
min_value = statistics.min(float_list)

# Max_value = max(float_list)
Max_value = statistics.max(float_list)


# Print the results
print("Total sum of all numbers: " + str(total_num))
print("Average (mean) of all numbers: " + str(average))
print("minimum value: " + str(min_value))
print("Maximum value: " + str(Max_value))
