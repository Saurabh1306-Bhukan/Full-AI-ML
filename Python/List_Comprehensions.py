# [output for item in iterable if condition]


sq = [i*i for i in range(6) if i%2 != 0]
print(sq)


nums = [-2, -1, 3, 4, -3, 7]

nums = [0 if val < 0 else val for val in nums]
print(nums)


words = ["python", "is", "a", "programming", "language"]

words = [val.upper() for val in words]
print(words)
