
sum_ids = 0
with open("input.txt", "r") as f:
    for line in f:
        id_ranges = line.split(',')
    for id_range in id_ranges:
        id_vals = id_range.split('-')
        id_start_str = id_vals[0]
        id_stop_str = id_vals[1]
        id_start_val = int(id_vals[0])
        id_stop_val = int(id_vals[1])

        current_id = id_start_val

        while current_id <= id_stop_val:
            num_digits = len(str(current_id))
            if num_digits % 2 == 0:
                mid_char = int(num_digits / 2)
                prefix = str(current_id)[0:mid_char]
                int_prefix = int(prefix)
                invalid_id = prefix + prefix
                if int(invalid_id) in range(id_start_val, id_stop_val + 1):
                    sum_ids += int(invalid_id)
                int_prefix += 1
                invalid_id = str(int_prefix) + str(int_prefix)
                current_id = int(invalid_id)
            else:
                current_id_str = "1" + num_digits * "0"
                current_id = int(current_id_str)
    print(sum_ids)
