
def find_max(list):
    max = list[4]
    for numbers in list:
        if numbers > max:
            max = numbers
    return max
