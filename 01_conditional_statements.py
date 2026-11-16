# Python Fundamentals - Conditional Statements

# 1. Electricity Bill Calculator
units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Units cannot be negative.")
else:
    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = (100 * 5) + (units - 100) * 7
    else:
        bill = (100 * 5) + (200 * 7) + (units - 300) * 10

    if bill > 2000:
        bill = bill + (bill * 0.05)

    print("Total electricity bill: Rs.", round(bill, 2))


# 2. Loan Approval System
salary = float(input("\nEnter monthly salary: "))
credit_score = int(input("Enter credit score: "))
age = int(input("Enter age: "))

if salary >= 30000 and credit_score >= 700 and 21 <= age <= 60:
    print("Loan Approved")
elif salary >= 25000 and credit_score >= 650 and 21 <= age <= 60:
    print("Conditionally Approved")
else:
    print("Loan Rejected")


# 3. Number Classification
number = int(input("\nEnter a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

if number == 0:
    print("Zero is even")
elif number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")


# 4. Exam Result Analyzer
marks = []
for i in range(5):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

if any(mark < 0 or mark > 100 for mark in marks):
    print("Please enter marks between 0 and 100.")
elif any(mark < 33 for mark in marks):
    print("Result: Fail")
else:
    percentage = sum(marks) / 5
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 60:
        print("Division: First")
    elif percentage >= 50:
        print("Division: Second")
    elif percentage >= 40:
        print("Division: Third")
    else:
        print("Pass, but division is not specified in the assignment.")
