def recursive_max(lst):
    # Base case: if the list has only one element, return that element
    if len(lst) == 1:
        return lst[0]
    
    # Recursive case: compare the first element with the result of the rest of the list
    return max(lst[0], recursive_max(lst[1:]))

# Example usage
numbers = [1, 4, 5, 3]
result = recursive_max(numbers)
print(result)  # Output: 5
