import random 

def blank_painting():
    painting = {
    "blue" : random.choice([True, False]),
    "pink" : random.choice([True, False]),
    "green" : random.choice([True, False]),
    "red" : random.choice([True, False]),
    "yellow" : random.choice([True, False]),
    }
    return painting



def two_reds(p1, p2, p3):
    red_count = 0
    if p1["red"]:
       red_count += 1
    if p2["red"]:
       red_count += 1
    if p3["red"]:
        red_count += 1
    return red_count == 2


def blue_pink(p1, p2, p3):
    pink_blue_count = 0
    if p1["blue"] and p1["pink"]:
       pink_blue_count += 1
    if p2["blue"] and p2["pink"]:
        pink_blue_count += 1
    if p3["blue"] and p3["pink"]:
        pink_blue_count += 1
    return pink_blue_count == 1

def yellow_not_blue_green(p1, p2, p3):
    if p1["yellow"]:
        if p1["blue"] or p1["green"]:
            return False
    if p2["yellow"]:
        if p2["blue"] or p2["green"]:
            return False
    if p3["yellow"]:
        if p3["blue"] or p3["green"]:
            return False
    return True

while True:
    p1 = blank_painting()
    p2 = blank_painting()
    p3 = blank_painting()
    if not blue_pink(p1, p2, p3):
        continue
    if not two_reds(p1, p2, p3):
        continue
    if not yellow_not_blue_green(p1, p2, p3):
        continue
    print(p1, p2, p3)
    break
