# Intro 

# how you create a list

numbers = [1, 2, 3, 4, 5]
numbers.append(8) # adds an element on the list
numbers.insert(0, 20) # inserts the element on specified index
numbers.remove(5) # removes the specified element
pooped_numbers = numbers.pop(2) # remove the item in the indicated index
more_numbers = [90, 50] # extra list
numbers.extend(more_numbers) # add the extra list to the original list
print(numbers)
sliced_numbers = numbers[0:3:2] # prints from index 0 to 3 and if you add the two it will print from 0 to 2
print(sliced_numbers)

for number in numbers:
    print(numbers)

print(len(numbers))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
index = numbers.index(4)
print(index)

present = 4 in numbers
print(present)

presents = 30 in numbers
print(presents)


numbers =[1,2,3,4,5,6,7,3,3,4,2,5,6,3,3,2,2,3]

count = numbers.count(3)
print(count)

numbers.sort()
print(numbers)
