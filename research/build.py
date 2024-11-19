# map function
numbers = [1, 2, 3, 4, 5]

doubled = map(lambda x: x * 2, numbers)

print(list(doubled))  


# filter function

numbers = [1, 2, 3, 4, 5, 6]

evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))  


#  zip function
# 
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]


paired = zip(names, scores)

print(list(paired))  