from random import shuffle

doors = ['goat', 'goat', 'car']
simulation_count = 100000
fail = 0
success = 0

for x in range(simulation_count):
    shuffle(doors)

    d1, d2, d3 = doors[0], doors[1], doors[2]

    if d1 == 'goat':
        if d3 == 'car':
            success += 1
        else:
            fail += 1

    else:
        success += 1

print(str(round(100*(success/simulation_count), 2)) + '%')
