
# a prime number is one which is divisible by itself and one.
# suppose I have a number 5;
# 5: divisible only by 1 and 5 itself, so it is a prime number
# 4: divisible by 1, 4 and 2 also, so it is not a prime number


def check_if_prime(number):
    output = "not a prime number"
    if number == 1:
        print(output)
    for i in range(2, number):
        if number % i == 0:
            print(output)
            exit()

    else:
        output = "is a prime number"
        print(output)


check_if_prime(91)
