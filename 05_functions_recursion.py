# Python Fundamentals - Functions and Recursion

# 1. Factorial using a loop
def factorial_loop(number):
    if number < 0:
        return None

    answer = 1
    for i in range(1, number + 1):
        answer *= i
    return answer


num = int(input("Enter a number for factorial: "))
result = factorial_loop(num)

if result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial:", result)


# 2. Sum of first n natural numbers using recursion
def natural_sum(n):
    if n <= 0:
        return 0
    return n + natural_sum(n - 1)


n = int(input("\nEnter n to find sum of natural numbers: "))
print("Sum:", natural_sum(n))


# 3. Reverse a string using recursion
def reverse_string(text):
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]


word = input("\nEnter a string to reverse: ")
print("Reversed string:", reverse_string(word))


# 4. Find x raised to power n using recursion
def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    return x * power(x, n - 1)


base = float(input("\nEnter base: "))
exponent = int(input("Enter exponent: "))
print("Answer:", power(base, exponent))
