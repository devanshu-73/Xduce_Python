# List , Tuple , Dictionary , Set
# =======================================================================================================

# List

# =======================================================================================================
# Q - 1 : How do you iterate over elements in a list using loops in Python
# =======================================================================================================

l1 = [1,'d',3.23,'e',5,'v',7]

# forloop
for i in l1:
    print(i) 

# whileloop
i = 0
while i < len(l1):
    print(l1[i])
    i += 1


# =======================================================================================================
# Q - 2 : How do you sort a list in Python? Explain different sorting techniques available.
# Q - 3 : Can you explain the difference between list.sort() and sorted() functions
# =======================================================================================================

l2 = [2,1,4,5,7,3,0]

# ======================================================================================================
# Way 1 : Using Own logic

for i in range(len(l2)):
    for j in range(len(l2)-1):
        if l2[j] > l2[j+1]:
             l2[j],l2[j+1] = l2[j+1],l2[j]

print('Sorted List :',l2)

# ======================================================================================================

# Way 2 : using Sort Method list.sort() 

'''
    sort() :  It modifies Original list means inplace sorting
'''
l2.sort()
print('Sorted List Using Sort() :',l2)

# ======================================================================================================

# Way 3 : using Sorted Method sorted(list)

'''
    sorted() :  It return new list
'''
n2_l2 = sorted(l2)
print('Sorted List Using Sorted() :',n2_l2)

# =======================================================================================================
# Q  - 4  : How do you find the length of a list in Python
# =======================================================================================================

l3 = [1,2,4,5,7,8]

# Way 1 : Own Logic
count = 0

for i in l3:
    count +=1

print("Length :",count)

# Way 2 : Using len Method

print('Length of List :',len(l3))



# =======================================================================================================

# Tuple

# =======================================================================================================
# Q  - 1  : How do you create an empty tuple in Python
# =======================================================================================================

t1 = ()
print('Empty Tuple :',t1)

# =======================================================================================================

# Q - 2 : Can you modify the elements of a tuple after it has been created? Why or why not?
''' 
    No it is not Possible Bcz Tuples are immutable,
    meaning once they are created, you cannot modify the elements within them
'''

# =======================================================================================================

# Q - 3 : Explain the concept of indexing in tuples. How do you access elements in a tuple using indexing?

'''
Indexing in tuples allows you to access individual elements based on their position.
It starts from 0, with tuple_name[index].
Negative indexing accesses elements from the end.
tuple_name[-1] return the last element.
'''

t1 = (1,2,3,4,5,6)

print(t1[0]) # first Element
print(t1[-1]) # Last Element

# =======================================================================================================

# Q - 4 : How do you convert a tuple into a list, and vice versa?

t2 = (11,22,33,44,55,66)

# Tuple to List Conversion

list1 = list(t2)
print(list1)

# List to Tuple Conversion

list2 = [11,22,33,44,55]
tuple1 = tuple(list2)
print(tuple1)

# =======================================================================================================

# Dictionary

# =======================================================================================================
# Q - 1 : How do you create an empty dictionary in Python?

empty_dict = {}
# or 
empty_dict = dict()

# =======================================================================================================
# Q - 2 : Explain the difference between dict.keys(),dict.values(), and dict.items() methods.

d1 = {'name': 'Dev', 'age': 15, 'marks': {'maths': 95, 'physics': 89, 'chemistry': 85}}

# dict.keys() : we can access all keys of dictionary 

for k in d1.keys():
    print(k)

# dict.values() : we can access all values of dictionary 

for v in d1.values():
    print(v)

# dict.items() : we can access both keys and values of dictionary 

for k,v in d1.items():
    print(f'{k}:{v}')

# =======================================================================================================

# Q - 3 : How do you iterate over key-value pairs in a dictionary using loops in Python?

for k,v in d1['marks'].items():
    print(f'{k}:{v}')

# =======================================================================================================

# Q - 4 : What are dictionary comprehensions? Provide an example

'''
    Dictionary comprehensions are a concise and expressive way to create dictionaries in Python using a compact syntax. 
    it returns dictionary
    variable = {key_expression: value_expression for item in iterable}
'''

squares = {f'square of {x}': x*x for x in range(1, 6)}
print(squares)

# =======================================================================================================

# Sets

# =======================================================================================================

# Q - 1 : How do you add elements to a set in Python?
'''
    Using Add() Method We Can Add Elements In Set 
'''
s1 = {1,2,3,4,5}

s1.add(5)
print(s1)

# =======================================================================================================

# Q - 2 : Explain the difference between set.add() and set.update() methods.

'''
   Add() : Using Add() Method We Can Add Elements In Set 
   Update() : Using Update() Method We Can Add Multiple Elements In Set 
'''
s2 = {11,22}

# Adding a single element
s2.add(66)

# Adding multiple elements
s2.update([44,55])

print(s2)  

# =======================================================================================================

# Q - 3 : What are set comprehensions? Provide an example.

'''
    Set comprehensions are a concise and efficient way to create sets in Python using a compact syntax
    it returns Set
    variable = {expression for item in iterable}
'''

squares = {x*x for x in range(1, 6)}
print(squares)
