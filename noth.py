emoji = {
    ":)": "😁",
    ":(": "😢"
}
out =''
x = input(" ").split(' ')
for item in x:
        out += emoji.get(item, item) + ' '
print(out)
