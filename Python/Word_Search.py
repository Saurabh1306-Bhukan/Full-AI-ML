data = True
line = 1
word = "Python"

with open (r"E:\AI_ML (Cource)\Python\sample4.txt", "r") as f:
    while data:      
        data = f.readline()
        if("Python" in data):
            print(f"{word} found at line {line}")
            break
        print(data)
        line +=1

    
