# Day 1: Python Basics - SOLUTIONS
# Reference after attempting practice.py

# ============================================================
# EXERCISE 1: Variables & Data Types
# ============================================================

name = "Vishal"
age = 28
height = 5.9
is_student = True
skills = ["Python", "Git", "AWS"]
profile = {"name": name, "age": age, "skills": skills}

print("--- Exercise 1: Variables & Types ---")
for var, val in [("name", name), ("age", age), ("height", height), 
                  ("is_student", is_student), ("skills", skills), ("profile", profile)]:
    print(f"{var} = {val} | type: {type(val).__name__}")

# ============================================================
# EXERCISE 2: Basic Operators
# ============================================================

print("\n--- Exercise 2: Operators ---")
a, b = 10, 3
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}  (floor division)")
print(f"a % b = {a % b}    (modulo)")
print(f"a ** b = {a ** b}  (exponentiation)")

# ============================================================
# EXERCISE 3: String Operations
# ============================================================

print("\n--- Exercise 3: Strings ---")
text = "  Hello, Python!  "
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Replace: '{text.replace('Python', 'World')}'")
print(f"Split: {text.split()}")
print(f"F-string: Name={name}, Age={age}")

# ============================================================
# EXERCISE 4: Input/Output (commented for auto-run)
# ============================================================

print("\n--- Exercise 4: I/O (demo) ---")
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}, you are {age} years old.")
print("(Skipped input in auto-run)")

# ============================================================
# EXERCISE 5: Conditionals
# ============================================================

print("\n--- Exercise 5: Conditionals ---")
for number in [-5, 0, 7]:
    if number > 0:
        result = "positive"
    elif number < 0:
        result = "negative"
    else:
        result = "zero"
    print(f"{number} is {result}")

# ============================================================
# EXERCISE 6: Loops
# ============================================================

print("\n--- Exercise 6: Loops ---")
print("For loop 1-5:", end=" ")
for i in range(1, 6):
    print(i, end=" ")
print()

print("Countdown:", end=" ")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print()

fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# ============================================================
# MINI CHALLENGE: Calculator
# ============================================================

print("\n--- Mini Challenge: Calculator ---")
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                return "Error: Division by zero!"
            result = num1 / num2
        else:
            return f"Error: Unknown operator '{op}'"
        
        return f"Result: {num1} {op} {num2} = {result}"
    except ValueError:
        return "Error: Invalid number input"

# Uncomment to run interactively:
# print(calculator())
print("(Run calculator() interactively)")

print("\n✅ Day 1 complete! Run: python practice.py")