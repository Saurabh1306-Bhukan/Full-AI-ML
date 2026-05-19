# Dictionary :- Key:Value pair
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

info = {
    "name": "John",
    "cgpa": 9.5,
    "subjects": ["Math", "Physics", "Chemistry"],
    3.14: "pi"
}

print(type(info))  
print(info.items())  # returns a view object that displays a list of dictionary's key-value tuple pairs
print(info.keys())  # returns a view object that displays a list of all the keys in the dictionary
print(info.values())  # returns a view object that displays a list of all the values in the dictionary  
print(info.get("name"))  # returns the value of the specified key
print(info.update({"age": 25}))  # adds a key-value pair to the dictionary

print(info)

