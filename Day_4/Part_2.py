def check_neighbors(row_num, col_num):
    num_neighbors = 0
    if row_num == 0:
        if col_num == 0:
            if lines[row_num][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num + 1] == "@":
                num_neighbors += 1
        elif col_num == num_cols - 1:
            if lines[row_num][col_num - 1] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num - 1] == "@":
                num_neighbors += 1
        else:
            if lines[row_num][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num][col_num - 1] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num - 1] == "@":
                num_neighbors += 1
    elif row_num == num_rows - 1:
        if col_num == 0:
            if lines[row_num][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num + 1] == "@":
                num_neighbors += 1
        elif col_num == num_cols - 1:
            if lines[row_num][col_num - 1] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num - 1] == "@":
                num_neighbors += 1
        else:
            if lines[row_num][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num][col_num - 1] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num - 1] == "@":
                num_neighbors += 1
    else:
        if col_num == 0:
            if lines[row_num][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num + 1] == "@":
                num_neighbors += 1
        elif col_num == num_cols - 1:
            if lines[row_num][col_num - 1] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num - 1] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num - 1] == "@":
                num_neighbors += 1
        else:
            if lines[row_num][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num][col_num - 1] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num - 1][col_num - 1] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num + 1][col_num - 1] == "@":
                num_neighbors += 1
    if num_neighbors < 4:
        return True
    else:
        return False


with open("input.txt", "r") as f:
    lines = f.readlines()
    num_cols = len(lines[0].rstrip())
    num_rows = len(lines)
    new_lines = []
    looping = True
    total_rolls = 0
    while looping:
        num_rolls = 0
        for i in range(0, num_rows):
            new_lines_string = ""
            for j in range(0, num_cols):
                sym = lines[i][j]
                if sym == "@":
                    if check_neighbors(i, j):
                        num_rolls += 1
                        new_lines_string += "X"
                    else:
                        new_lines_string += sym
                else:
                    new_lines_string += "."
            new_lines.append(new_lines_string)
        if num_rolls == 0:
            looping = False
        else:
            lines = []
            lines = new_lines
            new_lines = []
        total_rolls += num_rolls
    print(total_rolls)
