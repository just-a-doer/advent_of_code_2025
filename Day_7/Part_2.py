
with open("input.txt", "r") as f:
    lines = f.readlines()
    beams = set([lines[0].find('S')])
    grid_width = len(lines[0])
    grid_height = len(lines)

    num_beams = 0
    for line in lines:
        current_beams = beams.copy()
        for beam in current_beams:
            if line[beam] == '^':
                num_beams += 2
                beams.remove(beam)
                right_beam = beam + 1
                left_beam = beam - 1
                if right_beam < grid_width:
                    beams.add(right_beam)
                if left_beam >= 0:
                    beams.add(left_beam)

    print(num_beams)






