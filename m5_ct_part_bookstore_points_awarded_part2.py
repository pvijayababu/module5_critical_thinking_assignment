'''
The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:

If a customer purchases 0 books, they earn 0 points.
If a customer purchases 2 books, they earn 5 points.
If a customer purchases 4 books, they earn 15 points.
If a customer purchases 6 books, they earn 30 points.
If a customer purchases 8 or more books, they earn 60 points.'''
# Program to calculate and display points based on books purchased

# Ask the user to enter the number of books purchased this month
print('Welcome to CSU Global Book store')
print('For number of books purchased, please only enter even numbers between 0 to 8 or more')
books_purchased = int(input("Enter the number of books purchased this month: "))

# Determine the points awarded based on the number of books purchased
if books_purchased == 0:
    points_awarded = 0
elif books_purchased == 2:
    points_awarded = 5
elif books_purchased == 4:
    points_awarded = 15
elif books_purchased == 6:
    points_awarded = 30
elif books_purchased >= 8:
    points_awarded = 60
else:
    points_awarded = 0  # For any other number of books not explicitly listed

# Display the points awarded
print(f"Points awarded: {points_awarded}")