def recursive_sum(lst, index):
    # Base case: if index is 0, return the first element
    if index == 0:
        return lst[0]
    
    # Recursive case: sum current element with sum of previous elements
    return lst[index] + recursive_sum(lst, index - 1)

# numbers = [4, 3, 1, 5]
# index = 1
# result = recursive_sum(numbers, index)
# print(result)  # Output: 7 

numbers = [1, 4, 5, 3, 12, 16]
index = 4
result = recursive_sum(numbers, index)
print(result)  # Output: 25
