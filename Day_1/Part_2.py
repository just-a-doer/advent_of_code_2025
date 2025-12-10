
def check_sign(number):
    if number >= 0:
        return True
    elif number < 0:
        return False

num_zeros = 0

orig_dial_loc = 50
with open("input.txt", "r") as f:
    for line in f:
        dist_str = line[1:]
        dist = int(dist_str)
        if line[0] == "L":
            dial_loc = orig_dial_loc - dist
        elif line[0] == "R":
            dial_loc = orig_dial_loc + dist

        num_revolutions = abs(int(dist/100))
        if (dial_loc < 0 and orig_dial_loc != 0) or dial_loc > 100:
            num_zeros += 1
        elif dial_loc == 0:
            num_zeros += 1
        elif dial_loc == 100:
            num_zeros += 1
        if num_revolutions > 1:
            num_zeros += num_revolutions
        orig_dial_loc = dial_loc % 100


    print(num_zeros)





