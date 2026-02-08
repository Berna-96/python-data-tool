def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def calculate_max(numbers):
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum

def calculate_min(numbers):
    minimum = numbers[0]
    for n in numbers:
        if n < minimum:
            minimum = n
    return minimum

def count_numbers(data):
    return len(data)

numbers = [10, 5, 8, 20, 3]

print("Average:", calculate_average(numbers))
print("Maximum:", calculate_max(numbers))
print("Minimum:", calculate_min(numbers))
print("Total numbers:", count_numbers(numbers))
