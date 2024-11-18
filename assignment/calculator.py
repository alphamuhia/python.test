# Write a python program that does simple calculations

def calculator():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed."

    def multiply(a, b):
        return a * b

    def square(a):
        return a * a

    def square_root(a):
        return a ** 0.5

    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Square")
    print("6. Square Root")

    choice = int(input("Enter the number of the operation: "))

    if choice in [1, 2, 3, 4]:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", subtract(a, b))
        elif choice == 3:
            print("Result:", divide(a, b))
        elif choice == 4:
            print("Result:", multiply(a, b))
    elif choice == 5:
        a = float(input("Enter the number: "))
        print("Result:", square(a))
    elif choice == 6:
        a = float(input("Enter the number: "))
        print("Result:", square_root(a))
    else:
        print("Invalid choice. Please try again.")

print(calculator())
