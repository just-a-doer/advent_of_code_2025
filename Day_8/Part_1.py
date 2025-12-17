import math

closest_point_list = []
def find_closest_point(target_point, points_list):
    """
    Finds the point in points_list that is closest to the target_point.
    """
    dist_list = []
    # Define a key function to calculate the squared distance
    def squared_distance(point):
        x1, y1, z1 = target_point
        x2, y2, z2 = point
        return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

    for point in point_list:
        if point != target_point:
            dist_list = []
            dist = squared_distance(point)
            dist_list.append(target_point)
            dist_list.append(point)
            sorted_dist_list = sorted(dist_list, key=lambda x: x[0])
            sorted_dist_list.append(dist)
            if sorted_dist_list not in closest_point_list:
                closest_point_list.append(sorted_dist_list)
    return dist


with open("input.txt", "r") as f:
    lines = f.readlines()
    point_list = []
    for line in lines:
        line = line.split(',')
        int_list = [int(item) for item in line]
        point_list.append(int_list)

# Example Usage:
for i in range(0,len(point_list)):
    target = point_list[i]
    points = point_list.copy()
    del points[i]
    find_closest_point(target, points)

sorted_list = sorted(closest_point_list, key=lambda x: x[2])
if sorted_list[0][1] == sorted_list[1][2]:
    print("true")

light_string = []
light_string_lists = []
num_connections = 0

for j in range(0,len(sorted_list)):
    if num_connections < 10:
        connection_list = []
        first_loc = sorted_list[j][0]
        second_loc = sorted_list[j][1]
        found = False
        for k in range(0,len(light_string_lists)):
            if first_loc in light_string_lists[k] and second_loc in light_string_lists[k] and not found:
                found = True
                continue
            elif first_loc in light_string_lists[k] and not found:
                found = True
                light_string_lists[k].append(second_loc)
                num_connections += 1
            elif second_loc in light_string_lists[k] and not found:
                found = True
                light_string_lists[k].append(first_loc)
                num_connections += 1

        if not found:
            connection_list.append(first_loc)
            connection_list.append(second_loc)
            light_string_lists.append(connection_list)
            num_connections += 1
print(num_connections)
