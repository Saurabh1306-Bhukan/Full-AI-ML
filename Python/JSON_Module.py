# JSON : JavsCRIPT Object Notation

# JSON is a lightweight data-interchange format. 
# It is easy for humans to read and write.
# It is easy for machines to parse and generate. 
# It is based on a subset of the JavaScript Programming Language, Standard ECMA-262 3rd Edition - December 1999. 
# JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. 
# These properties make JSON an ideal data-interchange language.


import json

json_str = '{"name": "Saurabh", "isStudent": true}'

py_obj = json.loads(json_str)
print(type(py_obj), py_obj) 


py_obj = {
    "name": "Saurabh",
    "isStudent": True
}

py_obj = json.dumps(py_obj)
print(type(json_str), json_str)


with open(r"E:\AI_ML (Cource)\Python\Data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)

print("================================")

data = {
    "name": "Saurabh",
    "age": 23,
    "isTeeacher": True
}

with open ("E:\AI_ML (Cource)\Python\Data.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)
