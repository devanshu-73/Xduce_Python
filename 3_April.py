# ==================================================================================================================
# Topic 1 : Args & Kwargs
# ==================================================================================================================
 
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
    Subject: Logout Details for Today

Hi Shivam Sir,

I trust your day was productive.

Logout Time: [Insert time, e.g., 6:00 PM]

Task Update: Yes, I have completed all the tasks mentioned at login successfully.

Extra Work: Furthermore, I dedicated some time to familiarize myself with the pandas library and the logging library for better debugging and error tracking.

Looking forward to applying these new skills in future tasks.

Best regards,
'''

def args_kwargs_fn(*args, **kwargs):
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)

args_kwargs_fn(11, 22, 33, Name='Dev_anshu', Age=24)


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

# ==================================================================================================================
# Topic 3 : Lambda Functions
# ==================================================================================================================

# Example 1 : Basic Addition With 2 Values

add = lambda x,y : x+y
add(1,2)

# Example 2 : Addition With Multiple Values

add = lambda *args : sum(args)
add(1,2,3,4,5,6,7,8,9)

# Example 3 : Odd,Even With List

list1 = [1,2,3,4,5,6,7,8,9]

even = list(filter(lambda x : x % 2 == 0,list1)) # Getting Even list
odd = list(filter(lambda x : x % 2 != 0,list1)) # Getting Odd List
print("Even : ",even)
print("Odd : ",odd)