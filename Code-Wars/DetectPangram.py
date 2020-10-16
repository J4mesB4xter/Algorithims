import string
from string import ascii_lowercase

def is_pangram(s):
    x = 0
    for i in string.ascii_lowercase:
        if s.count(i) >= 1:
            x = x + 1
    if x is 26:
        return True
    else:
        return False