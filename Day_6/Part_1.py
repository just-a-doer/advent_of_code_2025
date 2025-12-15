import math
total = 0
with open("input.txt", "r") as f:
    lines = [line.rstrip('\n') for line in f]
    problem_array = []
    for i in range(len(lines)):
        cleaned_list = [item for item in lines[i].split(' ') if item.strip()]
        problem_array.append(cleaned_list)
    num_problems = len(problem_array[0])
    num_operators = len(problem_array)

    for i in range(0,num_problems):
        operators = []
        operation = problem_array[num_operators-1][i]
        for j in range(0,num_operators-1):
            operators.append(int(problem_array[j][i]))
        if operation == "*":
            total += math.prod(operators)
        elif operation == "+":
            total += sum(operators)
    print(total)





