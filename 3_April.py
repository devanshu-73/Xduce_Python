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

print("==============================================================================")

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

print("==============================================================================")

# Example Of *Args & **KWArgs together in a function definition to accept both positional and keyword arguments:

def args_kwargs_fn(*args, **kwargs):
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)

args_kwargs_fn(11, 22, 33, Name='Dev_anshu', Age=24)
