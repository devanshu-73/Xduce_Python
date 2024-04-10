# List Comprehension , Lambda Function, Generators

# 1) List Comprehension : Get Even numbers from list 

nums = [22,33,44,55,66,77,88,99]
even_nums =  [num for num in nums if num%2 == 0]
# print("Even Numbers :",even_nums)

# 2) Lambda Function : Get Odd Numbers

odd_nums = lambda nums: [num for num in nums if num%2 != 0]
# print("Odd Numbers :",odd_nums(nums)) 

# 3) Generators Function :
def countdown(n):
    while n > 0:
        yield n
        print("==========",n)
        n -= 1

# print(countdown(5)) # It Returns Object 

# Using the generator

# Way 1 :To Print
num = countdown(5)
# U can print single elements using next(num)
print(next(num))
# Whole List 
print(list(num))

# Way 2 :To Print
for num in countdown(5):
    print(num)
