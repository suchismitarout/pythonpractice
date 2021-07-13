def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)


factorial(5)
def factorial_recur(n):
    if n == 1:
        return n
    else:
        return n *factorial_recur(n-1)

print(factorial_recur(5))
