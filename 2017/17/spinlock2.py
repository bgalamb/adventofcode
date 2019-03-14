iteration_count = 50000000
step_size = 371

#spinlock = [0]
position = 0
spinlocklength = 1
for i in range(iteration_count):
    # 0 mod 371 = 371

    cut_index = (step_size + position) % (i+1)
    position = cut_index +1

    if position == 1 :
        print(i+1)
