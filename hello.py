import random

# write a hello function that prints "Hello, World!"
def hello():
    print("Hello, World!")

#invoke hello function
hello()

#write a decorator function logs input and output and times it to a function
def log(func):
    def wrapper(*args, **kwargs):
        print("Calling {} with arguments {}".format(func.__name__, args))
        result = func(*args, **kwargs)
        print("{} returned {}".format(func.__name__, result))
        return result
    return wrapper

#invoke decorator function using hello function
@log
def hello(x):
    print(f"Hello, World! {x}")

hello(3)

# write a function that yields a generator that randomly picks between three types of fruit
def fruit_generator():
    fruits = ["apple", "banana", "orange"]
    while True:
        yield fruits[random.randint(0, 2)]


 #invoke fruit_generator function and print the result of the generator for five runs
for i in range(5):
    print(next(fruit_generator()))
