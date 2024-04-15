# ==================================================================================================================
# Topic 2 : Decorators
# ==================================================================================================================

# Sample Example 

def decorator_fn(fn):
    def wrapper(*args,**kwargs):
        print("Before")   # If u want do something before Main function  
        fn()              # Main Function Which going to be decorate
        print("After")    # or U can do something after Main Function
    return wrapper

@decorator_fn
def going_to_decorate():
    print('Hello Everyone....')  

going_to_decorate()

# Decorator Example : 1 

def deco_add(func):
    def wrapper(*args):
        print("Arguments:", args)
        result = func(*args)
        print("Result:", result)
        return result
    return wrapper

@deco_add
def add(a, b):
    return a + b

result = add(3, 5)