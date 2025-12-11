
battery_val = 0
total_power = 0
with open("input.txt", "r") as f:
    for line in f:
        battery_power_str_list = []
        for battery in line:
            if len(battery_power_str_list) < 12:
                battery_power_str_list.append(battery)
            else:
                battery_power = int(battery_power_str_list[0]+battery_power_str_list[1])
                new_battery_power1 = int(battery_power_str_list[0]+battery)
                new_battery_power2 = int(battery_power_str_list[1]+battery)
                max_new_power = max(new_battery_power1,new_battery_power2)
                if max_new_power >= battery_power:
                    final_power = max_new_power
                    battery_power_str_list[0] = str(final_power)[0]
                    battery_power_str_list[1] = str(final_power)[1]
                else:
                    final_power = battery_power
        total_power += final_power
    print(total_power)

