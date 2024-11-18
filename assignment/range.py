# Write a python program to check if a number is in a given range

def range(num,start,end):
    if start <= num <= end:
        return True
    else:
        False

num = int(input("Enter the number to ckeck: "))
start = int(input("Enter the first number of the range: "))
end = int(input("Enter last number of the range: "))

if range(num,start,end):
    print("Number is within range.")
else:
    print("Number is not within range.")