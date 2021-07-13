def print_fibonacci(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
        print("provide valid positive number")
    elif n == 1:
        print(n1)
    else:
        while count < n:
            print(n1, end=' ')
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


print_fibonacci(9)

print("\n")


def print_fibonacci_recur(n):
    if n < 0:
        return "provide positive number"
    if n == 0:
        return n
    if n == 1:
        return n

    return print_fibonacci_recur(n - 1) + print_fibonacci_recur(n - 2)


print(print_fibonacci_recur(9))
