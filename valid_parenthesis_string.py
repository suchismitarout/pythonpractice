def is_valid_parenthese(str1):
    first_stack = []
    sec_stack = []
    for k, v in enumerate(str1):
        if v == '(':
            first_stack.append(k)
        if v == ')':
            if first_stack:
                first_stack.pop()
            elif sec_stack:
                sec_stack.pop()
            else:
                return False
        if v == '*':
            sec_stack.append(k)

    if not len(sec_stack) >= len(first_stack):
        return False
    while first_stack:
        if first_stack.pop() > sec_stack.pop():
            return False
    return True


print(is_valid_parenthese("(*))"))

