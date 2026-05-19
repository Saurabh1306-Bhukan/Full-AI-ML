# Tuples 
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# immutable sequence of values 

tup = (1, 2, 3, 4, 5)

print(tup[:])  # slicing the tuple from index 0 to the end  

# using loop

sum = 0
for val in tup:
    sum += val
print("The sum is:", sum)

# --------------------Methods of tuple------------------
# count() :- returns the number of times a specified value occurs in a tuple

tup2 = (1, 2, 3, 4, 5, 1, 2, 1)
print(tup2.count(1))  # counts the number of times 1 occurs in

# index() :- searches the tuple for a specified value and returns the position of where it was found

print(tup2.index(3))  # returns the index of the first occurrence of
