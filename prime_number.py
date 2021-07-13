def prime_number(input_number):
    for i in range(2, input_number):
        if input_number % i == 0:
            print("its not a prime number")
            break
    else:
        print("its a prime number")


prime_number(11)
