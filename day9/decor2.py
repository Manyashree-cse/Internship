'''/*def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def greet():
    print("Hello")
greet()'''

def my_decorator(greet):
    def wrapper():
        print("Before function")
        greet()
        print("After function")
    return wrapper

@my_decorator
def greet():
    print("Hello")
greet()