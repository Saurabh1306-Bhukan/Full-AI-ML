# Lists :-  mutable sequence of values
# Lists are ordered, changeable, and allow duplicate values.

marks = [99, 89, 100, 65, 92, "abc", 100.90]

print(marks)
print(len(marks))  # length of the list

print(type(marks))  # type of the list



# ----------------------------------------------
# slicing of list

print("-------------------slicing------------------")

print(marks[0:3])  # slicing the list from index 0 to 2 

# -----------------------------------------------
# List methods
print("-------------------List methods------------------")

# append() :- adds an element to the end of the list
marks.append(85)
print(marks)

# insert() :- adds an element at a specific position in the list
marks.insert(2, 95)  # insert 95 at index 2
print(marks)

# remove() :- removes the first occurrence of an element from the list
marks.remove(100)  # removes the first occurrence of 100
print(marks)

# pop() :- removes and returns the last element of the list
last_element = marks.pop()  # removes and returns the last element
print("Last element removed:", last_element)
print(marks)

# sort() :- sorts the list in ascending order
# marks.sort()  # this will give an error because the list contains different data types
# print(marks)


# ------------------------------------------------
# List with loops

print("-------------------list with loops------------------")

nums = [1, 2, 3, 4, 10, 5]

x = 10
idx = 0

for val in nums:
    if (val == x):
        print(f"x found at idx = {idx}")
        break
    idx += 1
    

