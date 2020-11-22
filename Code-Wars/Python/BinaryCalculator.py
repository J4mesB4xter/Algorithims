def Calculate(a, b):
    y = input("choose an operator (+, -, *, /")
    if y == "+":
        return a + b
    elif y == "-":
        return a - b
    elif y == "*":
        return a * b
    elif y == "/":
        return a / b
    else:
        return "invalid operator"