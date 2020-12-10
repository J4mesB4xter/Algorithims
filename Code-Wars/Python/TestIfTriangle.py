def IsTriangle(a, b, c):
    if a + b <= c, a + c <= b, b + c <= a:
        return False
    else:
        return True