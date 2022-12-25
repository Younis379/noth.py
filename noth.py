def positive_sum(arr):
    conc = []
    for item in arr:
        if item > 0:
            conc.append(item)
    return conc


print(positive_sum([2, -4, 1, -4, 5]))