
def yield_example():
    n = 1
    print("this is first")
    yield n

    n += 1
    print("this is second")
    yield n

    n += 1
    print("this is third")
    yield n


for i in yield_example():
    print(i)

# y = yield_example()
# next(y)
# next(y)
#
# next(y)