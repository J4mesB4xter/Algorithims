def FindMiddleElement(input_array):
    n = sorted(input_array)
    return input_array.index(n[round(len(input_array)/2)-1])