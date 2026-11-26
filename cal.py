
import math

# Professional Scientific Calculator

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return math.sqrt(a)

def percentage(a, b):
    return (a * b) / 100

def factorial(a):
    if a < 0 or not a.is_integer():
        raise ValueError("Enter a non-negative integer!")
    return math.factorial(int(a))

def logarithm(a):
    if a <= 0:
        raise ValueError("Logarithm requires a positive number!")
    return math.log10(a)

def show_menu():
    print("\n" + "=" * 40)
    print("       PROFESSIONAL CALCULATOR")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Factorial")
    print("9. Logarithm (Base 10)")
    print("0. Exit")
    print("=" * 40)

while True:

    show_menu()

    choice = input("Select your operation: ").strip()

    if choice == "0":
        print("Thank you for using the calculator!")
        break

    try:

        if choice in ["1", "2", "3", "4", "5", "7"]:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = addition(num1, num2)

            elif choice == "2":
                result = subtraction(num1, num2)

            elif choice == "3":
                result = multiplication(num1, num2)

            elif choice == "4":
                result = division(num1, num2)

            elif choice == "5":
                result = power(num1, num2)

            elif choice == "7":
                result = percentage(num1, num2)

        elif choice in ["6", "8", "9"]:

            num1 = float(input("Enter a number: "))

            if choice == "6":
                result = square_root(num1)

            elif choice == "8":
                result = factorial(num1)

            elif choice == "9":
                result = logarithm(num1)

        else:
            print("Invalid choice! Select between 0 and 9.")
            continue

        print("\nResult:", result)

    except (ValueError, ZeroDivisionError, OverflowError) as error:
        print("Error:", error)

    except Exception as error:
        print("Unexpected error:", error)
