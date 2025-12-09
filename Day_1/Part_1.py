
dial_loc = 50
num_zeros = 0
with open("input.txt", "r") as f:
    for line in f:
        if line[0] == "L":
            direction = -1
        elif line[0] == "R":
            direction = 1
        dist_str = line[1:]
        dist = direction * int(dist_str)
        dial_loc += dist
        if(dial_loc % 100) == 0:
            num_zeros += 1
    print(num_zeros)


