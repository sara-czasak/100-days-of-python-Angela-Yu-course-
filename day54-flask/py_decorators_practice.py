import time

# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function

def wait(function):
    def wrapper():
        function()
        function()
    return wrapper

@wait
def say_hello():
    print('hello')

@wait
def say_bye():
    print('goodbye')

@wait
def ask():
    print('How are you?')

