def make_pallindrome(input_string):
    input_string = list(input_string)
    length = len(input_string)
    counter = 0
    for i in range(length):
        if input_string[i] != input_string[length-1-i]:
            counter +=1
            if input_string[i] < input_string[length-1-i]:
                input_string[length-1-i] = input_string[i]
            else:
                input_string[i] = input_string[length-1-i]
    print(''.join(input_string))
    print("{} minimum characters to be replaces".format(counter))



make_pallindrome('geeks')

