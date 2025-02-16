def decor(func):

    def wrapper(*args):
        result = func(*args)
        print(result)
    return wrapper


@decor
def calc(first, second):
    if first == second:
        return first + second
    #if operation == '+':
    #    return first + second
    elif first > second:
        return first - second
    elif second > first:
        return first / second
    elif first < 0 and second < 0:
        return first * second
    else:
        print('Incorrect numbers')
        return

a = (int)(input('Input first number: '))
b = (int)(input('Input second number: '))
calc(a, b)
