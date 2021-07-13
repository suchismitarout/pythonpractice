def sort_in_desceding(input_list):
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] < input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]

    print(input_list)


sort_in_desceding([56, 1, 23, 67, 13, 89])


def sort_in_ascending(input_list):
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] > input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]

    print(input_list)


sort_in_ascending([23, 12, 34, 10, 15, 1])
