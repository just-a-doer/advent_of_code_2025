sum_ids = 0

bad_id_array = []
def check_char_pattern(num_char):
    pattern = current_val_str[0:num_char]
    start_loc = num_char
    if start_loc >= len(current_val_str):
        return False
    while start_loc < len(current_val_str):
        substr = current_val_str[start_loc:start_loc+num_char]
        if pattern != substr:
            return False
        start_loc += num_char
    return True


with open("input.txt", "r") as f:
    for line in f:
        id_ranges = line.split(',')
    for id_range in id_ranges:
        id_vals = id_range.split('-')
        id_start_str = id_vals[0]
        id_stop_str = id_vals[1]

        start_val = int(id_start_str)
        stop_val = int(id_stop_str)

        current_val = start_val
        while current_val <= stop_val:
            current_val_str = str(current_val)
            for i in range(1,20):
                if len(current_val_str) >= 2*i:
                    valid = check_char_pattern(i)
                    if valid:
                        bad_id_array.append(current_val)
                        unique_list = list(set(bad_id_array))
            current_val += 1
    print(sum(unique_list))
