
def check_neighbors(row_num,col_num):
    num_neighbors = 0
    if row_num == 0:
        if col_num == 0:
            if lines[row_num][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num+1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num+1][col_num+1] == "@":
                num_neighbors += 1
        elif col_num < num_cols-1:
            if lines[row_num][col_num + 1] == "@":
                num_neighbors += 1
            if lines[row_num][col_num - 1] == "@":
                num_neighbors += 1
            if lines[row_num+1][col_num] == "@":
                num_neighbors += 1
            if lines[row_num+1][col_num+1] == "@":
                num_neighbors += 1
            if lines[row_num+1][col_num-1] == "@":
                num_neighbors += 1
    return num_neighbors






with open("input.txt", "r") as f:
    lines = f.readlines()
    num_cols = len(lines[0].rstrip())
    num_rows = len(lines)
    for i in range(0,num_rows):
        for j in range(0,num_cols-1):
            sym = lines[i][j]
            if sym == "@":
                num_rolls = check_neighbors(i,j)
                print(num_rolls)

