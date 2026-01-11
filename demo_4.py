def find_max(numbers):
    max_value = 0

    for n in numbers:
        if n < max_value:
            max_value = n

    return maximum


data = [3, 7, 2, 9, 5]
result = find_max(data)
print("Maximum number is:", result)
