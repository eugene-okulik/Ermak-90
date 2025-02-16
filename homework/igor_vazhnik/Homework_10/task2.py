def repeat_me(func):

    def wrapper(*args, **kwargs):
        while kwargs['count'] > 0:
            func(*args)
            kwargs['count'] -= 1

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
