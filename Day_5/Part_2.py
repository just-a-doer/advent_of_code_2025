num_good = 0
with open("input.txt", "r") as f:
    lines = f.readlines()
    sorted_range_array = []
    final_range_array = []
    for line in lines:
        included = False
        line = line.rstrip()
        if "-" in line:
            range_list = []
            ranges = line.split('-')
            range_list.append(int(ranges[0]))
            range_list.append(int(ranges[1]))
            sorted_range_array.append(range_list)
            sorted_range_array.sort(key=lambda x: x[0])
    current_range = sorted_range_array[0]
    for i in range(0, len(sorted_range_array)-1):
        range_set = []
        if sorted_range_array[i + 1][0] <= current_range[1] <= sorted_range_array[i + 1][1]:
            start_range = current_range[0]
            stop_range = sorted_range_array[i+1][1]
            range_set.append(start_range)
            range_set.append(stop_range)
            current_range = range_set
        elif sorted_range_array[i + 1][0] <= current_range[1] > sorted_range_array[i + 1][1]:
            continue
        else:
            range_set = sorted_range_array[i+1]
            final_range_array.append(current_range)
            current_range = range_set
    final_range_array.append(current_range)


    num_good = 0
    for j in range(0,len(final_range_array)):
        num_good += final_range_array[j][1]-final_range_array[j][0]+1
    print(num_good)


