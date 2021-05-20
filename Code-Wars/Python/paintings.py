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

def two_reds(*paintings):
    red_count = 0
    for p in paintings:
        if p["red"]:
            red_count += 1
    return red_count == 2


def blue_pink(*paintings):
    pink_blue_count = 0
    for p in paintings:
        if p["blue"] and p["pink"]:
            pink_blue_count += 1
    return pink_blue_count == 1

def pink_not_green(*paintings):
    for p in paintings:
        if not p["pink"] and not p["green"]:
            return False
    return True

def yellow_not_blue_green(*paintings):
    for p in paintings:
        if p["yellow"]:
            if p["blue"] or p["green"]:
                return False
    return True

def every_color(*paintings):
    has_yellow = False
    has_red = False
    has_pink = False
    has_green = False
    has_blue = False
    for p in paintings:
        if p["yellow"]:
            has_yellow = True
        if p["red"]:
            has_red = True
        if p["pink"]:
            has_pink = True
        if p["green"]:
            has_green = True
        if p["blue"]:
            has_blue = True
    return has_pink and has_green and has_blue and has_yellow and has_red

while True:
    p1 = blank_painting()
    p2 = blank_painting()
    p3 = blank_painting()
    if not every_color(p1,p2, p3):
        continue
    if not pink_not_green(p1, p2, p3):
        continue
    if not blue_pink(p1, p2, p3):
        continue
    if not two_reds(p1, p2, p3):
        continue
    if not yellow_not_blue_green(p1, p2, p3):
        continue
    print(p1, p2, p3)
    break
