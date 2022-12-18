list = [2, 4, 6, 4, 2, 5, 8, 9, 10, 14, 17, 74, 2, 3, 2, 2, 32]
out =[]
for item in list:
    if item not in out:
        out.append(item)
print(out)
