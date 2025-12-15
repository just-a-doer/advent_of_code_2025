
def check_fresh(value):
    if value < min_range or value > max_range:
        return False
    else:
        for j in range(0,len(range_start_list)):
            if value >= range_start_list[j] and value <= range_stop_list[j]:
                return True

num_fresh = 0
with open("input.txt", "r") as f:
    lines = f.readlines()
    range_start_list = []
    range_stop_list = []
    for line in lines:
        included = False
        line = line.rstrip()
        if "-" in line:
            ranges = line.split('-')
            for i in range(0,len(range_start_list)):
                if int(ranges[0]) >= range_start_list[i] and int(ranges[1]) <= range_stop_list[i]:
                    included = True
            if not included:
                range_start_list.append(int(ranges[0]))
                range_stop_list.append(int(ranges[1]))
        elif line == "":
            min_range = min(range_start_list)
            max_range = max(range_stop_list)
        else:
            ingredient = int(line)
            if check_fresh(ingredient):
                num_fresh += 1
    print(num_fresh)



