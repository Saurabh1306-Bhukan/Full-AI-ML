# while loop 


count = 1

while (count <= 10):
    print("hello world", count)
    count += 1

print("after loop, count =", count)


# -----------------------------------------------

i = 1

while (i<=5):
    print(i)
    i += 1


# -----------------------------------------------
n = int(input("Enter a number: "))
j = 1

while(j <= 10):
    print(n*j)
    j += 1


# --------------------------------------------------

# Break & Continue statement :- 

# break statement : terminates the loop completely
# continue statement : skips the current iteration and moves to the next iteration


a = 1

while (a <= 10):
    if (a % 6 == 0):
        break
    print(a)
    a += 1

print("outside loop now....")


# --------------------------------------------------

c = 1
while (c <= 10):
    if (c % 3 == 0):
        c += 1
        continue
    print(c)
    c += 1


# --------------------------------------------------
print("-------------------For loop-------------------")

for i in range(5):
    print(i)


word = "artificial intelligence"

# count the number of i's >= 5

count = 0

for ch in word:
    if (ch == 'i'):
        count += 1

print("count of i = ", count)

# --------------------------------------------------

# QS. print vowels count of a given string.

word1 = "artificial"

count1 = 0

for ch in word1:
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count1 += 1

print("count of vowels = ", count1)

# --------------------------------------------------

# Range() : generates a sequence of numbers
# range(start, stop, step)

for i in range(1, 11):
    print(i)


# QS. print sum of first 'n' natural numbers.

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i

print (sum)

