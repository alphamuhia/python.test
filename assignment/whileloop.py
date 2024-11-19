# import random

# def generate(start, end):
#     return random.randint(start, end)


# answer = generate(1, 100)

# print("for a price guess a number between 1 and 100? ")

# while True:
#     choice = int(input("Enter your guess: "))
#     if choice < answer:
#         print("Your guess is smaller than the answer.")
#     elif choice > answer:
#         print("Your guess is larger than the answer.")
#     else:
#         print("You are correct!")
#         break 


# # sum of numbers

# current_number = 1
# total_sum = 0

# # Use a while loop to calculate the sum
# while current_number <= 500:
#     total_sum += current_number
#     current_number += 1

# print("The sum of numbers from 1 to 500 is:", total_sum)

# # print triangle

# # Number of rows for the triangle
# rows = 15
# current_row = 1

# # Outer loop for each row
# while current_row <= rows:
#     # Print stars equal to the current row number
#     print("*" * current_row)
#     current_row += 1

# # nested loop

# # Number of rows for the triangle
# rows = 15

# # Outer loop for rows
# for i in range(1, rows + 1):
#     # Inner loop for columns
#     for j in range(i):
#         print("*", end="")
#     # Move to the next line after each row
#     print()


