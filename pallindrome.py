def pallindrome(num_):
    rev = 0
    temp = num_
    while num_:
        d = num_ % 10
        rev = rev * 10 + d
        num_ = num_ // 10

    if rev == temp:
        print("its a pallindrome number")
    else:
        print("its not")



pallindrome(121)

