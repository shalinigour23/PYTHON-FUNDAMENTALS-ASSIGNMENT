# Python Fundamentals - Error and Exception Handling

# 1. Age Validation System
try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("Age accepted.")
except ValueError as error:
    print("Invalid age:", error)


# 2. Bank Withdrawal System
balance = 5000

try:
    amount = float(input("\nEnter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    if amount > balance:
        raise ValueError("Withdrawal amount exceeds available balance.")

    balance -= amount
    print("Withdrawal successful.")
    print("Remaining balance:", balance)
except ValueError as error:
    print("Transaction failed:", error)


# 3. Password Validator with custom exceptions
class ShortPasswordError(Exception):
    pass


class UppercaseMissingError(Exception):
    pass


class NumberMissingError(Exception):
    pass


password = input("\nCreate a password: ")

try:
    if len(password) < 8:
        raise ShortPasswordError("Password must contain at least 8 characters.")

    if not any(character.isupper() for character in password):
        raise UppercaseMissingError("Password must contain an uppercase letter.")

    if not any(character.isdigit() for character in password):
        raise NumberMissingError("Password must contain a number.")

    print("Password is valid.")

except (ShortPasswordError, UppercaseMissingError, NumberMissingError) as error:
    print("Password error:", error)
