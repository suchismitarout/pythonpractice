def merge_sort(list1, r):
    if len(list1) > 1:
        mid = len(list1)//2
        left = list1[:mid]
        right = list1[mid:]
        merge_sort(left, r)
        merge_sort(right, r)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i].__getattribute__(r) < right[j].__getattribute__(r):
                list1[k] = left[i]
                i += 1
            else:
                list1[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list1[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list1[k] = right[j]
            j += 1
            k += 1
    return list1


class Employee:
    def __init__(self, id, sal):
        self.id = id
        self.sal = sal

    def __repr__(self):
        return "id:{}, sal:{}".format(self.id, self.sal)

e1 = Employee(2,30000)
e2 = Employee(15, 45558)
e3 = Employee(3, 25000)
e4 = Employee(7, 27000)
e5 = Employee(1, 24000)


# print(dir(e5))
# print(e5.__getattribute__("sal"))
def emp_sort(em_list, sal):
    return merge_sort(em_list, sal)
print(emp_sort([e1,e2,e3,e4,e5],'sal'))