def find_max(numbers):
    max_value = float('-inf')  # Initialize to negative infinity

    for n in numbers:
        if n > max_value:  # Change comparison to find the maximum
            max_value = n

    return max_value  # Corrected the return variable name

data = [3, 7, 2, 9, 5]
result = find_max(data)
print("Maximum number is:", result)  # CodeSentinal: created for you by RuchirAdnaik.