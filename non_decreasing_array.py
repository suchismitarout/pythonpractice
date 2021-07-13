def non_decreasing_list(num_list):
    for i in range(len(num_list)):
        if num_list[i] < num_list[i+1] and num_list == sorted(num_list):
            print(True)
        else:


non_decreasing_list([4, 2, 3])
