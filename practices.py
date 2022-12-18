
while True:
    answer = input(">").lower()
    if answer =="start":
        print("car ready to go")
        break
    elif answer =="stop":
        print("car is stopping")
        break
    elif answer == "help":
        print("""
start-to start
 stop-to stop
 quit-to quit""")
    elif answer=="quit":
        break
    else:
        print("i don't understand that")
