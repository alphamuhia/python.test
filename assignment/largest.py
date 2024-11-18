# Write a program to find the largest among three numbers.

def large(firstnum, secondnum, thirdnum):
    if firstnum >= secondnum and firstnum >= thirdnum:
        return f"{firstnum} is the largest number."
    elif secondnum >= firstnum and secondnum >= thirdnum:
        return f'{secondnum} is the largest number'
    else:
        return f"{thirdnum} is the largest number"

firstnum = int(input("Enter first number: "))
secondnum = int(input("Enter second number: "))
thirdnum = int(input("Enter third number: "))

print(large(firstnum, secondnum, thirdnum))

