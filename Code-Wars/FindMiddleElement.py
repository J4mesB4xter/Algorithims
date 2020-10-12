#code wars tasked me with finding the middle element in lists 
#of three, but after accomplishing that i went ahead and 
#made a code that would work on larger lists as well.
#a list of three is so specific that it seemed necessary to 
#abstract and find a more reusable function

def gimme(input_array):
    n = sorted(input_array)
    return input_array.index(n[round(len(input_array)/2)-1])
