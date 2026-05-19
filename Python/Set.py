# Set: A collection of unique elements
# A set is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.

set1 = {1, 2, 2, 3, 4, 5}
print(set1)
print(len(set1))  # returns the number of items in the set
# set does not allow duplicate values


# set does not support indexing, slicing, or other sequence-like behavior
# set1[0]  # this will raise an error

# methods: 

set1.add(6)  # adds an element to the set
print(set1)
set1.remove(2)  # removes an element from the set
print(set1)
# set1.clear()  # removes all elements from the set
# print(set1)
set1.pop()  # removes a random element from the set and returns it
print(set1)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 8, 9, 10}

print(s1.union(s2)) # returns a new set that is the union of two sets

print(s1.intersection(s2))  # returns a new set that is the intersection of two sets
