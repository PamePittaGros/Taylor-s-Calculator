# calculator.py
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by 0"
    return a / b

def square_root(a):
    if a < 0:
        return "Error: negative number"
    return math.sqrt(a)

def power(a, b):
    return a ** b

def run_calculator():
    print("Simple calculator: choose operation")
    print("add, subtract, multiply, divide, sqrt, power, quit")
    while True:
        op = input("operation: ").strip().lower()
        if op in ("quit", "q", "exit"):
            print("Goodbye.")
            break
        if op == "sqrt":
            x = float(input("number: "))
            print("=", square_root(x))
            continue
        if op in ("add", "subtract", "multiply", "divide", "power"):
            a = float(input("first number: "))
            b = float(input("second number: "))
            if op == "add":
                print("=", add(a, b))
            elif op == "subtract":
                print("=", subtract(a, b))
            elif op == "multiply":
                print("=", multiply(a, b))
            elif op == "divide":
                print("=", divide(a, b))
            elif op == "power":
                print("=", power(a, b))
            continue
        print("Unknown operation. Try again.")

if __name__ == "__main__":
    run_calculator()
