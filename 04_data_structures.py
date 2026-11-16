# Python Fundamentals - List, Tuple, Set and Dictionary

# 1. Rotate a list left or right by k positions
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

k = int(input("Enter number of positions to rotate: "))
direction = input("Enter L for left or R for right: ").upper()

if numbers:
    k = k % len(numbers)
    if direction == "L":
        rotated = numbers[k:] + numbers[:k]
    elif direction == "R":
        rotated = numbers[-k:] + numbers[:-k] if k != 0 else numbers[:]
    else:
        rotated = numbers[:]
        print("Invalid direction. Original list kept.")
    print("Rotated list:", rotated)


# 2. Remove duplicates without using set
values = [1, 2, 3, 2, 4, 1, 5, 3]
unique_values = []

for value in values:
    if value not in unique_values:
        unique_values.append(value)

print("\nList without duplicates:", unique_values)


# 3. Find missing number from 1 to n
numbers = [1, 2, 4, 5, 6]
n = 6
expected_total = n * (n + 1) // 2
missing_number = expected_total - sum(numbers)
print("Missing number:", missing_number)


# 4. Tuple of five subjects
subjects = ("Python", "Mathematics", "Physics", "English", "Computer Science")
print("\nThird subject:", subjects[2])
print("Total subjects:", len(subjects))
print("Index of Physics:", subjects.index("Physics"))


# 5. Convert tuple pairs to dictionary
pairs = ((1, "A"), (2, "B"), (3, "C"))
pair_dictionary = dict(pairs)
print("\nDictionary:", pair_dictionary)


# 6. Swap first and last tuple elements without converting to list
sample_tuple = (10, 20, 30, 40, 50)
first, *middle, last = sample_tuple
swapped_tuple = (last, *middle, first)
print("\nTuple after swapping first and last:", swapped_tuple)


# 7. Subset checker
set_a = {2, 4}
set_b = {1, 2, 3, 4, 5}

if set_a.issubset(set_b):
    print("\nFirst set is a subset of second set.")
else:
    print("\nFirst set is not a subset of second set.")


# 8. Student Marks Analyzer
student_marks = {
    "Aman": 78,
    "Riya": 92,
    "Karan": 65,
    "Neha": 29
}

topper = max(student_marks, key=student_marks.get)
average = sum(student_marks.values()) / len(student_marks)
failures = []

for name, mark in student_marks.items():
    if mark < 33:
        failures.append(name)

print("\nTopper:", topper, "-", student_marks[topper])
print("Class average:", round(average, 2))
print("Students who failed:", failures)


# 9. Library Management using dictionary
library = {
    "Python Basics": 4,
    "Data Structures": 2,
    "Computer Networks": 3
}

print("\nCurrent library:", library)
book = input("Enter book name to issue: ")

if book in library and library[book] > 0:
    library[book] -= 1
    print("Book issued successfully.")
else:
    print("Book is not available.")

print("Updated library:", library)
