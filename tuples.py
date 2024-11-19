# tuples are immutable, heterogeneous, orderd and indexes. They are created using ()

single_tuple = (12,)
empty_tuple = ()
print(empty_tuple)
name = ("name",)
print(type(name))

name = (1,2,3,4)

students = ('mark' 'peter', 'mark', 'mercy')
print(students.count('mark'))
print(students.index('mercy'))
print(students*3)
print('peter' in students)
print(len(students))
for students in students:
    print(students)

more = ('john', 'james', 'joy')

print(more)

tuple1 = (1, 2, 3, 4)

a, b , c, d = tuple1

print(a)

list_1 = list(tuple1)
print(list_1)
list_1.append(5)
print(list_1)

tuple_1 = tuple(list_1)

print(tuple_1)