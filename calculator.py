def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "not possible"


def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "not possible"


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))


print("Addition:", add(n1, n2))
print("Subtraction:", subtract(n1, n2))
print("Multiplication:", multiply(n1, n2))
print("Division:", divide(n1, n2))
print("Modulus:", modulus(n1, n2))
