
with open("input.txt", "r") as f:
    lines = f.readlines()
    start_beam  = lines[0].find('S')
    grid_width = len(lines[0])
    grid_height = len(lines)

    path_lists = [start_beam]
    new_beam_lists = []
    path_set = set(path_lists)
    duplicates = 0
    for index in range(1,len(lines)):
        print(index)
        line = lines[index]
        for path in path_lists:
            beam = path
            if line[beam] == '^':
                right_beam = beam + 1
                left_beam = beam - 1
                if right_beam < grid_width:
                    new_beam_lists.append(right_beam)
                if left_beam >= 0:
                    new_beam_lists.append(left_beam)
            else:
                new_beam_lists.append(beam)
        path_lists = new_beam_lists.copy()
        path_set = set(path_lists)
        duplicates += len(path_lists)-len(path_set)
        new_beam_lists.clear()

print(len(path_lists))
print(path_lists)
path_set = set(path_lists)
print(path_set)
# final_path_list = [path_lists[0]]
# j = 0
# for path in path_lists:
#     j += 1
#     print(j)
#     for i in range(0,len(final_path_list)):
#         if path != final_path_list[i]:
#             final_path_list.append(path)












