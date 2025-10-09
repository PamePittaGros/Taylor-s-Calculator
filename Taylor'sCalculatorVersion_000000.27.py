import math     #Let me math

#How we functions + - * /
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Handle dividing by zero
    if b == 0:
        return "Error: cannot divide by 0"
    return a / b

def square_root(a):
    return math.sqrt(a)

def power(a, b):
    return a ** b

# Example usage
print(add(5, 3))          # 8
print(subtract(10, 4))    # 6
print(multiply(2, 6))     # 12
print(divide(8, 2))       # 4.0
print(divide(5, 0))       # Error message
print(square_root(16))    # 4.0
print(power(2, 3))        # 8




































