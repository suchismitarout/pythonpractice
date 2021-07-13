def exception_handle(n):
    try:
        return n // 2
    except TypeError:
        return "please enter an integer"
    except ZeroDivisionError :
        return "please enter greater than 0"
    finally:
        return n

# print(exception_handle("som"))
# print(exception_handle(0))
print(exception_handle(15))


