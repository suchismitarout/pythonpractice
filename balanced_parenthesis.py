def balanced_parenthesis(string1):
    stk = []
    open = ['(', '{', '[']
    close = [')', '}', ']']
    for i in string1:
        if i in open:
            stk.append(i)
        elif i in close:
            pos = close.index(i)
            if len(stk) > 0 and open[pos] == stk[len(stk) - 1]:
                stk.pop()
            else:
                return "unbalanced"
    if len(stk) == 0:
        return "balanced"
    else:
        return "unbalanced"


print(balanced_parenthesis('({})[]'))


def balanced_parenthesis_queue(string1):
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))
    queue = []

    for i in string1:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return "Unbalanced"
    if not queue:
        return "Balanced"
    else:
        return "Unbalanced"


print(balanced_parenthesis_queue('{()[]'))
