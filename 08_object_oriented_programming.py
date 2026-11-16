# Python Fundamentals - Object Oriented Programming

# 1. Multilevel inheritance: Vehicle -> Car -> ElectricCar
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_vehicle(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def show_details(self):
        self.show_vehicle()
        print("Model:", self.model)
        print("Battery:", self.battery, "kWh")


print("1. Multilevel inheritance")
my_car = ElectricCar("Tata", "Nexon EV", 40)
my_car.show_details()


# 2. Multiple inheritance: Teacher + Researcher -> Professor
class Teacher:
    def teach(self):
        print("Professor teaches students.")


class Researcher:
    def research(self):
        print("Professor works on research.")


class Professor(Teacher, Researcher):
    pass


print("\n2. Multiple inheritance")
professor = Professor()
professor.teach()
professor.research()


# 3. Hierarchical inheritance: Shape -> Circle, Rectangle, Triangle
class Shape:
    def description(self):
        print("This is a shape.")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


print("\n3. Hierarchical inheritance")
shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 4)]
for shape in shapes:
    shape.description()
    print("Area:", shape.area())


# 4. Method overriding: Animal -> Dog/Cat
class Animal:
    def sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def sound(self):
        print("Dog barks.")


class Cat(Animal):
    def sound(self):
        print("Cat meows.")


print("\n4. Method overriding")
Dog().sound()
Cat().sound()


# 5. Operator overloading: Add two complex numbers
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __str__(self):
        sign = "+" if self.imaginary >= 0 else "-"
        return str(self.real) + " " + sign + " " + str(abs(self.imaginary)) + "i"


print("\n5. Operator overloading")
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(2, 5)
print("Sum:", c1 + c2)


# 6. Class with private salary variable
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def show_salary(self):
        print("Salary:", self.__salary)


print("\n6. Private variable")
employee = Employee(35000)
employee.show_salary()


# 7. ATM system using encapsulation (PIN and balance are private)
class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_pin(self, entered_pin):
        return entered_pin == self.__pin

    def show_balance(self, entered_pin):
        if self.check_pin(entered_pin):
            print("Available balance:", self.__balance)
        else:
            print("Incorrect PIN.")

    def withdraw(self, entered_pin, amount):
        if not self.check_pin(entered_pin):
            print("Incorrect PIN.")
        elif amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Please collect your cash.")
            print("Remaining balance:", self.__balance)


print("\n7. ATM system")
atm = ATM(1234, 10000)
entered_pin = int(input("Enter ATM PIN: "))
atm.show_balance(entered_pin)
withdraw_amount = float(input("Enter amount to withdraw: "))
atm.withdraw(entered_pin, withdraw_amount)


# 8. Game Character Design
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def introduce(self):
        print(self.name, "has", self.health, "health points.")


class Warrior(Character):
    def attack(self):
        print(self.name, "attacks with a sword.")


class Wizard(Character):
    def attack(self):
        print(self.name, "casts a magic spell.")


class Archer(Character):
    def attack(self):
        print(self.name, "shoots an arrow.")


print("\n8. Game characters")
characters = [Warrior("Arjun", 100), Wizard("Mira", 80), Archer("Dev", 90)]
for character in characters:
    character.introduce()
    character.attack()
