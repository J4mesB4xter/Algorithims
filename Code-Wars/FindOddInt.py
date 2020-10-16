#given a list of integers where only one integer occurs an odd number of times, returns that integer


def find_it(seq):
    x = [i for i in seq if seq.count(i) % 2 != 0]
    return x[0]
