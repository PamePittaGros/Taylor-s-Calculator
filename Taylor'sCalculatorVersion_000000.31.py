import math  # Give me math.

# Let me functions
def add(a, b):
    return a + b

def subtract(a, b):  # Fixed spelling
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    #"Zero doesn't equal zero."
    if b == 0:
        return "Error - 0 is 0"
    return a / b

def square_root(a):
    return math.sqrt(a)

def power(a, b):
    return a ** b

# Helper function to get two numbers from the user
def get_two_numbers():
    a = float(input("First number: "))
    b = float(input("Second number: "))
    return a, b

# Main menu loop
while True:
    print("\n--- Taylor's Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Quit")

    choice = input("Choose (1-7): ")

    if choice == "1":
        a, b = get_two_numbers()
        print("Result:", add(a, b))

    elif choice == "2":
        a, b = get_two_numbers()
        print("Result:", subtract(a, b))  # Fixed spelling

    elif choice == "3":
        a, b = get_two_numbers()
        print("Result:", multiply(a, b))

    elif choice == "4":
        a, b = get_two_numbers()
        print("Result:", divide(a, b))  # Fixed spelling

    elif choice == "5":
        a = float(input("Number: "))
        print("Result:", square_root(a))

    elif choice == "6":
        a = float(input("Base: "))
        b = float(input("Exponent: "))
        print("Result:", power(a, b))

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Not a valid choice, try again.")
        