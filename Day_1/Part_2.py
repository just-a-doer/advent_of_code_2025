array_1 =[]
array_2 = []

def check_sign(number):
    if number >= 0:
        return True
    elif number < 0:
        return False


orig_dial_loc = 50
num_zeros = 0
with open("input.txt", "r") as f:
    for line in f:
        if line[0] == "L":
            direction = -1
        elif line[0] == "R":
            direction = 1
        dist_str = line[1:]
        dist_val = int(dist_str)
        num_rotations = int(dist_val/100)
        dist = direction * (int(dist_str) % 100)
        dial_loc = orig_dial_loc + dist

        sign_loc = check_sign(dial_loc)
        sign_orig_loc = check_sign(orig_dial_loc)

        if sign_loc != sign_orig_loc and orig_dial_loc != 0:
            num_zeros += 1
        elif dial_loc == 0:
            num_zeros += 1

        if dial_loc >= 100:
            num_rotations = int(dial_loc/100)
            dial_loc -= 100
        elif dial_loc < 0:
            dial_loc += 100
        print(dial_loc)
        if num_rotations > 0:
            num_zeros += num_rotations
        orig_dial_loc = dial_loc
    print(num_zeros)


