
numbers = {
    "1": "one",
    "2": "two",
    "3": "three"

}
output = ""
x = input("phone..")
for item in x:
   output += numbers.get(item, "!") + ' '
print(output)
