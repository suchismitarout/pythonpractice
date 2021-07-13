def reverse_list(num_list):
    h = []
    for i in range(len(num_list)):
        h.append(num_list.pop())
    print(h)


reverse_list([23,4,11,10,8,9,47])