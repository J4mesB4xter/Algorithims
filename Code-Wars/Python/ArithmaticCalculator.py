def Calculate(a, b):
    print("choose an operator (+, -, *, /")
    y = input("")
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

Calculate(17, 18)