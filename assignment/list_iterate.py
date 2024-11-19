# range
for numbres in range(1, 10):
    print(numbres >= 3)

# list

# map 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

check = map(lambda x: x >= 3, numbers)

print(list(check))

# filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

check = filter(lambda x: x > 3, numbers)

print(list(check))

# list method

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in numbers:
    print(x >= 3)