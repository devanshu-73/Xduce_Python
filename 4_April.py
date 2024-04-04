# List , Tuple , Dictionary , Set
# =======================================================================================================
# Q - 1 : How do you iterate over elements in a list using loops in Python
# =======================================================================================================


# forloop
for i in l1:
    print(i) 

# whileloop
l1 = [1,'d',3.23,'e',5,'v',7]
i = 0
while i < len(l1):
    print(l1[i])
    i += 1


# =======================================================================================================
# Q - 2 : How do you sort a list in Python? Explain different sorting techniques available.
# Q - 3 : Can you explain the difference between list.sort() and sorted() functions
# =======================================================================================================


l2 = [2,1,4,5,7,3,0]

# Tech 1 : Using Own logic

for i in range(len(l2)):
    for j in range(len(l2)-1):
        if l2[j] > l2[j+1]:
             l2[j],l2[j+1] = l2[j+1],l2[j]

print('Sorted List :',l2)

# Tech 2 : using Sort Method list.sort() 

'''
    sort() :  It modifies Original list means inplace sorting
'''
l2.sort()
print('Sorted List Using Sort() :',l2)

# Tech 3 : using Sorted Method sorted(list)

'''
    sorted() :  It return new list
'''
n2_l2 = sorted(l2)
print('Sorted List Using Sorted() :',n2_l2)


# =======================================================================================================
# Q  - 4  : How do you find the length of a list in Python
# =======================================================================================================

# using len Method

l3 = [1,2,4,5,7,8]
print('Length of List :',len(l3))
