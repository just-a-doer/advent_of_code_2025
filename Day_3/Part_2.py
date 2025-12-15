power = ""
final_power = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        steps = len(line)-12
        num_removed = 0
        power = line[:12]
        for j in range(0,steps):
            not_found = True
            i = 0
            while i < 11 and not_found:
                if power[i] < power[i+1]:
                    power = power[0:i] + power[i+1:] + line[12+j]
                    num_removed += 1
                    not_found = False
                i+=1
        for k in range(num_removed,steps):
            loc = len(line) - num_removed-1
            if line[loc-k] > power[11]:
                power = power[:-1]
                power += line[loc]

        final_power += int(power)
    print(final_power)




