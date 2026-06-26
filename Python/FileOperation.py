f = open(r"E:\AI_ML (Cource)\Python\sample.txt", "r")
data = f.read() # read the content of the file
#data= f.readline() # read the first line of the file

print(data)
print( )

f.close()

# write mode

f = open(r"E:\AI_ML (Cource)\Python\sample.txt", "w")
f.write("Text to overwite \n the complete data.")

f.close()

# append mode:
f = open(r"E:\AI_ML (Cource)\Python\sample.txt", "a")
f.write("\nText to appended \n the complete data.")

f.close()

# create new & open for writing mode  (x):

# f = open(r"E:\AI_ML (Cource)\Python\sample1.txt", "x")
# f.write("\nSome Random Text \nto create new text file.")

# f.close()



# b = binary mode
# t = text mode [default]
# + = opens disk file for update (r & w)

f = open(r"E:\AI_ML (Cource)\Python\sample.txt", "r+")
f.write("123,")
print(f.read())
f.close()

print("------------------------------")

f = open(r"E:\AI_ML (Cource)\Python\sample.txt", "a+")
f.write("123,")
print(f.read())
f.close()