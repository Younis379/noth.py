x = input("... ").split(' ')
def emoji():
    emoji = {
        ":)": "😁",
        ":(": "😢"
    }
    out = ''
    for item in x:
        out += emoji.get(item, item) + ' '
        return out

print(emoji())


