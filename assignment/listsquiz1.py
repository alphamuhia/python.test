# num = [1, 9, 30, 36, 58, 38, 38, 49, 85]

# # q1 laegest number
# large = max(num)
# print(large)

# # Q2 reverse list
# # num.reverse()
# # print(num)

# reverse = num[8:0:-1]
# print(reverse)

# # Q3 groceries list

# shop = ["potatoes", "tomatoes", "kales", "onions", "milk"]

# def shopping():
#     print("Choose an option:")
#     print("1. Add an item")
#     print("2. Remove an item")
#     print("3. Insert an item at a specific position")
#     print("4. View shopping list")
    
#     choice = int(input("Select function: "))
    
#     if choice == 1:  # Add an item
#         item = input("Enter the item to add: ")
#         shop.append(item)
#         print(f"{item} has been added to {shop}.")
#     elif choice == 2:  # Remove an item
#         item = input("Enter the item to remove: ")
#         if item in shop:
#             shop.remove(item)
#             print(f"{item} has been removed from {shop}.")
#         else:
#             print(f"{item} is not in {shop}.")
#     elif choice == 3:  # Insert an item
#         item = input("Enter the item to insert: ")
#         position = int(input("Enter the position (0-based index): "))
#         if 0 <= position <= len(shop):
#             shop.insert(position, item)
#             print(f"{item} has been inserted at position {position} in {shop}.")
#         else:
#             print("Invalid position.")
#     elif choice == 4:  # View the list
#         print("Current shopping list:")
#         for idx, item in enumerate(shop):
#             print(f"{idx}: {item}")
#     else:
#         print("Invalid choice. Please try again.")
    
#     more = input("Do you want to perform another operation? (yes/no): ").strip().lower()
#     if more == "y":
#         shopping()
#     else:
#         print("Goodbye!")

# shopping()
       