def loud(func):
    def wrapper(*args, **kwargs):
        print('Calling function')
        r = func(*args, **kwargs)
        print(f'function returned: {r}')
        print('done')

    return wrapper


@loud
def hi(name):
    return f'Hi {name}'


hi('you')


