# List , Tuple , Dictionary , Set

# Q - 1 : How do you iterate over elements in a list using loops in Python

l1 = [1,'d',3.23,'e',5,'v',7]
for i in l1:
    print(i) 


# Q - 2 : How do you sort a list in Python? Explain different sorting techniques available.

l2 = [2,1,4,5,7,3,0]

# Tech 1 : using Sort Method list.sort() 

l2.sort()
print(l2)

# Tech 2 : using Sorted Method sorted(list)

new_l2 = sorted(l2)
print(new_l2)


# Q  - 3: How do you find the length of a list in Python

# using len Method

l3 = [1,2,4,5,7,8]
print(len(l3))