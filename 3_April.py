# Topic 1 : Args & Kwargs
 
# Example Of *Args = Arguments
'''
    Taking Multiple Arguments at a time in 
    The Form of Tuple 
'''

def args_fn(*args):
    for arg in args:
        print(arg)

print("Args Output : ")
args_fn(1,2,3,4,5,6,7)


# Example Of **KWArgs = Keyword Arguments
'''
    Taking Multiple Arguments at a time in 
    The Form of Dictionary 
'''

def kwargs_fn(**kwargs):
    for k, v in kwargs.items():
        print(k,':', v)

print("KWArgs Output : ")
kwargs_fn(Name='Devanshu', Age=24, position='Python Trainee')


# Example Of *Args & **KWArgs 

'''
    we can use args,kwargs together in a function definition 
    to accept both 
    positional and keyword arguments
'''

def args_kwargs_fn(*args, **kwargs):
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)

args_kwargs_fn(11, 22, 33, Name='Dev_anshu', Age=24)



# Topic 2 : Decorators

def decorator_fn(fn,*args,**kwargs):
    def wrapper():
        print("Before : Doing Something")
        fn()
        print("After  : Doing Something")
    return wrapper

@decorator_fn
def going_to_decorate():
    print('Hello Everyone....')   

going_to_decorate()


