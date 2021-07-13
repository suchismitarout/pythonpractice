def zigzag_coversion(input_string, r):
    n = len(input_string)
    if n == 1:
        return
    res = ["" for i in range(n)]
    row = 0
    for i in range(n):
        res[row] += input_string[i]
        if row == r-1:
            down = False
        if row == 0:
            down = True

        if down:
            row += 1
        else:
            row -= 1


    for i in range(r):
        print(res[i], end="")

zigzag_coversion("PAYPALISHIRING", 3)