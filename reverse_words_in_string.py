def reverse_words_in_string(input_string):
    input_string = " ".join(input_string.split())
    input_string = input_string.split()
    k = []
    for i in range(len(input_string)):
        k.append(input_string.pop())
    print(" ".join(k))


reverse_words_in_string("  the sky is   blue  ")
