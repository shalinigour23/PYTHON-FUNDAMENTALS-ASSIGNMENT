# Python Fundamentals - Loops

# 1. Automorphic Number
number = int(input("Enter a number to check automorphic: "))
square = number * number

if str(square).endswith(str(number)):
    print(number, "is an automorphic number.")
else:
    print(number, "is not an automorphic number.")


# 2. Palindrome numbers in a given range
start = int(input("\nEnter starting number: "))
end = int(input("Enter ending number: "))

print("Palindrome numbers:")
for number in range(start, end + 1):
    if str(number) == str(number)[::-1]:
        print(number, end=" ")
print()


# 3. LCM and HCF using loops (without built-in functions)
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

a = abs(a)
b = abs(b)

if a == 0:
    hcf = b
elif b == 0:
    hcf = a
else:
    smaller = a if a < b else b
    hcf = 1
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            hcf = i

if a == 0 or b == 0:
    lcm = 0
else:
    larger = a if a > b else b
    lcm = larger
    while lcm % a != 0 or lcm % b != 0:
        lcm += larger

print("HCF:", hcf)
print("LCM:", lcm)


# 4. Password Retry System
correct_password = "Python123"
attempts = 0

while attempts < 3:
    entered_password = input("Enter password: ")
    if entered_password == correct_password:
        print("Login successful.")
        break
    else:
        attempts += 1
        print("Incorrect password. Attempts left:", 3 - attempts)

if attempts == 3:
    print("Account blocked after 3 failed attempts.")


# 5. Star patterns
rows = int(input("\nEnter number of rows for patterns: "))

print("\nTriangle:")
for i in range(1, rows + 1):
    print("* " * i)

print("\nPyramid:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

print("\nDiamond:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * (2 * i - 1))
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * (2 * i - 1))
