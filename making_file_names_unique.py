def get_folder_name(name_list):
    d = {}
    for name in name_list:
        if name in d:
            d[name] += 1
        else:
            d[name] = 1
    for k, v in d.items():
        if v > 1:
            for i in range(v - 1):
                name_list.append(k + str(v))
    print(name_list)


get_folder_name(["gta", "gta(1)", "gta", "avalon"])
