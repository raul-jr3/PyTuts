
a = [10, 20, 'nan', 30, 40, 'nan', 50]

def get_numbers(list_of_numbers):
    result = []
    for i in list_of_numbers:
        if i != str(i):
            result.append(i)
    print(result)

get_numbers(a)