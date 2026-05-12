# String :- it is a immutable


word1 = "I Love"
word2 = "Python"

print(len(word1))  # length of the string

print(word1 + " " + word2)  # concatenation of strings 


# Indexing:- 

print(word2[1]) # accessing the character at index 1

print( )

print(word2[-1]) # accessing the last character using negative indexing

# use for loop
print()

for ch in word2:
    print(ch)


# ------------------------------------------------
print("---------------------Slicing -------------------")

# Slicing :- 

word = "Hello Python"

print(word[0:5])  # slicing the string from index 0 to 4

print(word[6:])  # slicing the string from index 6 to the end



# -----------------------------------------------------
# String formatting :-

print("--------------------String Formating------------------")

a = 5
b = 10
sum = a + b

# normal formatting

print("language is {}".format("Python"))

print("sum of {} & {} is {}".format(a, b, sum))


# index based formatting

print("sum of {1} & {0} is {2}".format(a, b, sum))

# value based formatting

print("sum of {c} & {d}".format(c=4, d=3))



# ------------------------------------------------------
# f-strings :- literal string interpolation

print("--------------------F-strings------------------")


y = 5
z = 10

print(f"sum of {y} & {z} is {y+z}")
