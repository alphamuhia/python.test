# assignments

# q1. add several numbers

def add(a,b,c,d,e):
   return a + b + c + d + e 

a =4
b =3
c =9
d =7
e =8
print(add(a,b,c,d,e))

# q2. area
# circle
from math import pi

def areaofacircle(radius):
    return pi * radius ** 2

radius = 3
print(areaofacircle(radius))

#rectangle

def area_rec(length,width):
    return length*width

length = 7
width = 8

print(area_rec(length,width))

# triangle

def area_tri(base,height):
    return 1/2*base*height

base = 10
height = 9

print(area_tri(base,height))

#q3. factorial

from math import factorial

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n - 1)

n = 7
print(factorial(n))

# q4. multiplication

def multi(a,b,c,d,e,f):
    return a*b*c*d*e*f

a =3
b =4
c =6
d =9
e =2
f =5

print(multi(a,b,c,d,e,f))

   
# math functiode