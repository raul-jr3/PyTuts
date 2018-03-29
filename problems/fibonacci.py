
# fibonacci series:
# 0, 1, 1, 2, 3, 5, 8, 13....


def fibonacci(n):
    first = 0
    second = first + 1
    result = first + second
    print(first)
    print(second)
    for i in range(2, n):
        # print(first)
        # print(second)
        print(result)
        first = second
        second = result
        result = first + second
    # print(first, second)


fibonacci(8)
