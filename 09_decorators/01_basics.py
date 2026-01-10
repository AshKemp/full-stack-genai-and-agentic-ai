from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@my_decorator
def greet():
    print("Hello, from decorators class from chaicode")

greet()
print(greet.__name__)