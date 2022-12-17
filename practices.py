
secret_number = 10
limit_count = 3
guess_count = 1
while guess_count <= limit_count:
    answer = int(input("guess:"))
    if answer == secret_number:
        print("you won")
        break
    guess_count += 1
else:
    print("you lost")
