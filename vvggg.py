datalist = [{"name": "abc", "sal": 2000, "dept": "hr"}, {"name": "efg", "sal": 3000, "dept": "eng"},
            {"name": "hkm", "sal": 5000, "dept": "chem"}, {"name": "xyz", "sal": 5000, "dept": "phy"}]
datalist1 = [{"name": "abc", "sal": 2000, "dept": "hr"}, {"name": "plm", "sal": 5000, "dept": "math"},
             {"name": "hkm", "sal": 5000, "dept": "chem"}, {"name": "xyz", "sal": 7000, "dept": "phy"}]

not_updated = []
deleted = []
updated = []
new = []
for i in range(len(datalist)):
    if datalist[i] == datalist1[i]:
        not_updated.append(datalist[i])
    if datalist[i]["name"] not in datalist1[i]["name"]:
        deleted.append(datalist[i])
    if datalist[i]["name"] in datalist1[i]["name"] and datalist[i]not in not_updated:
        updated.append(datalist[i])
    if datalist1[i]["name"] not in datalist[i]["name"] and datalist1[i] not in updated:
        b=new.append(datalist1[i])



print(not_updated)
print(deleted)
print(updated)
print(new)