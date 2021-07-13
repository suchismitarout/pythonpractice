def func():
    num_list = [2,4,5,1]
    for i in num_list:
        print(i)


func()

k = func()
print(type(k))

def func1():
    num_list = [2, 4, 1, 8]
    for i in num_list:
        yield i


l = func1()
print(next(l))
print(next(l))
print(type(l))