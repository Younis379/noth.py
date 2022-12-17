
weight = input("weight: ")
type = input(f"'kg' or 'lbs'").lower()

if type == 'kg':
              converted= int(weight)/0.45
              print(f"you are {converted} pound.")

elif type == 'lbs':
                  converted = int(weight)*0.45
                  print(f"you are {converted} kilos. ")






