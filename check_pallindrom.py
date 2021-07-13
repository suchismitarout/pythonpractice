def check_pallindrom(input_num):
    temp = input_num
    rev = 0
    while input_num:
        digit = input_num % 10
        rev = rev * 10 + digit
        input_num = input_num // 10
    if rev == temp:
        return "its a pallindrom number"
    else:
        return "its not a pallindrom number"


print(check_pallindrom(121))
