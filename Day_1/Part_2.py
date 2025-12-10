
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
        num_revs = int(dist / 100)
        true_dist = dist - num_revs*100
        if line[0] == "L":
            dial_loc = orig_dial_loc - true_dist
            if dial_loc < 0 and orig_dial_loc != 0:
                num_zeros += 1
            num_zeros += num_revs
        elif line[0] == "R":
            dial_loc = orig_dial_loc + true_dist
            if dial_loc > 100:
                num_zeros += 1
            num_zeros += num_revs

        orig_dial_loc = dial_loc % 100
        if orig_dial_loc == 0:
            num_zeros += 1

    print(num_zeros)





