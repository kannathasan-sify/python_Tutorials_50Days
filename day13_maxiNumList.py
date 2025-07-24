# ListMaximum.py

def find_largest_number(numbers):
    if not numbers:
        return None  # Handle empty list

    largest = numbers[0]  # Assume first number is the largest initially

    for num in numbers:
        if num > largest:
            largest = num  # Update largest if current number is greater

    return largest

# Example usage
my_list = [10, 45, 67, 32, 89, 2,8940,900]
result = find_largest_number(my_list)
print("The largest number in the list is:", result)
