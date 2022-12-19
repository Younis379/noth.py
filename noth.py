try:
    age = int(input(">"))
    income =100
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('age must be more than zero')
except ValueError:
    print("invalid value")



