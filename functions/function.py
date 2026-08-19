def greet():
    print("Hello, welcome to Python!")

greet()

# function parameter
def greet(name):
    print("Hello", name)

greet("Chakri")

# fuction two parameter
def add(a, b):
    print("Sum =", a + b)

add(10, 20)

# even or odd 
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
print(even_odd(n))
# Positive, Negative or Zero
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

n = int(input("Enter a number: "))
print(check_number(n))



