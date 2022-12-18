started = False
while True:
    answer = input(">").lower()
    if answer == "start":
        if started:
            print("already satrted")
        else:
            print("car is ready to go")
    elif answer == "stop":
        if not started:
            print("car is already stopped")
        else:
            print("car is stopping")
    elif answer == "help":
        print("""
stop-to stop
start-to start
quit-to quit""")
    elif answer == "quit":
        break
    else:
        print("i don't understand this")

