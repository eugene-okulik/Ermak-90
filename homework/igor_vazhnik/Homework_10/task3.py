def decor(func):

    def wrapper(a, b):
        if a == b and a > 0 and b > 0:
            result = func(a, b, '+')
        elif a > b and a > 0 and b > 0:
            result = func(a, b, '-')
        elif a < b and a > 0 and b > 0:
            result = func(a, b, '/')
        elif a < 0 or b < 0:
            result = func(a, b,'*')
        print(result)
    return wrapper


@decor
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


a = (int)(input('Input first number: '))
b = (int)(input('Input second number: '))
calc(a, b)
