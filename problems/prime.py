

def check_if_prime(number):
    if number == 1:
        print("1 is not a prime number")
    for i in range(2, number):
        if number % i == 0:
            print("{} is not a prime number".format(number))
            exit()

    else:
        print("{} is a prime number".format(number))


        # else:
        #     print("{} is a prime number".format(number))
        #     exit()

check_if_prime(91)

