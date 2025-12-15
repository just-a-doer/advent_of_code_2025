import math
total = 0
line_array = []


def pad_left(num, string_val):
    new_string = string_val
    for index in range(0, num):
        new_string = "." + new_string
    return new_string


def pad_right(num, string_val):
    new_string = string_val
    for index in range(0, num):
        new_string += "."
    return new_string

operator_list = []
with open("input.txt", "r") as f:
    line_array = []
    clean_array = []
    lines = [line for line in f]
    for i in range(0, len(lines) - 1):
        line = lines[i].split(' ')
        line_array.append(line)
        cleaned_list = [item for item in line if item.strip()]
        clean_array.append(cleaned_list)
    num_cols = len(clean_array[0])

    line = lines[len(lines)-1].split(' ')
    operator_list = [item for item in line if item.strip()]

    col_width_array = []
    operator_array = []
    for j in range(0, num_cols):
        col_width_array.append(max(len(row[j]) for row in clean_array))

    val_str = ""
    val_str_array = []
    start_index = 0
    for row in lines:
        for width in col_width_array:
            val_str = row[start_index:start_index + width]
            val_str_array.append(val_str)
            start_index += width+1


#     row_index = 0
#     for row in line_array:
#         found_index = 0
#         for k in range(0, len(row)):
#             if row[k] != "":
#                 if len(row[k]) < col_width_array[found_index]:
#                     if k == 0:
#                         clean_array[row_index][found_index] = pad_right(
#                             col_width_array[found_index] - len(row[k]), row[k])
#                     elif k == len(row) - 1:
#                         if row[k - 1] == "":
#                             clean_array[row_index][found_index] = pad_left(
#                                 col_width_array[found_index] - len(row[k]), row[k])
#                         else:
#                             clean_array[row_index][found_index] = pad_right(
#                                 col_width_array[found_index] - len(row[k]), row[k].rstrip())
#                     elif row[k - 1] == "":
#                         clean_array[row_index][found_index] = pad_left(col_width_array[found_index] - len(row[k]),
#                                                                        row[k])
#                     elif row[k + 1] == "" or row[k + 1] == '\n':
#                         clean_array[row_index][found_index] = pad_right(
#                             col_width_array[found_index] - len(row[k]), row[k])
#                 found_index += 1
#         row_index += 1
#
#
# num_cols = len(clean_array[0])
# num_rows = len(clean_array)
#
# for col in range(0,num_cols):
#     operator = operator_list[col]
#     value_list = []
#     for idx in range(0,len(clean_array[0][col])):
#         value_str = ""
#         for row in range(0,num_rows):
#             if clean_array[row][col][idx] != "." and clean_array[row][col][idx] != '\n':
#                 value_str += clean_array[row][col][idx]
#         if value_str != "":
#             value_list.append(int(value_str))
#     if operator == "*":
#         total += math.prod(value_list)
#     elif operator == "+":
#         total += sum(value_list)
#
# print(total)
