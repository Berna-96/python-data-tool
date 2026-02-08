import csv

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

numbers = []

try:
    with open("data/numbers.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            numbers.append(int(row["value"]))

    print("Average:", calculate_average(numbers))
    print("Maximum:", calculate_max(numbers))
    print("Minimum:", calculate_min(numbers))
    print("Total numbers:", count_numbers(numbers))

except FileNotFoundError:
    print("Error: numbers.csv file not found.")

except ValueError:
    print("Error: invalid number in CSV file.")

