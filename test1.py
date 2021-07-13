def reverse_number(input_number):
    temp = input_number
    rev = 0
    while input_number:
        digit = input_number % 10
        rev = rev * 10 + digit
        input_number = input_number // 10
    return rev


print(reverse_number(123))
