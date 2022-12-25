def enough_space(cap, on, wait):
    if wait + on <= cap:
        return 0
    else:
        num_people_left = wait + on - cap
        print(f"{num_people_left} can't take")
    return


enough_space(10, 14, 12)
