''' Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
    The program should first ask for the number of years. 
    The outer loop will iterate once for each year. 
    The inner loop will iterate twelve times, once for each month. 
    Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
    After all iterations, the program should display the number of months, the total inches of rainfall, 
    and the average rainfall per month for the entire period.'''

# Program to calculate the average rainfall over a period of years

# Get the number of years from the user
number_of_years = int(input("Enter the number of years: "))

# Initialize variables to store the total rainfall and the number of months
total_rainfall = 0
total_months = 0

# Outer loop for each year
for year in range(1, number_of_years + 1):
    print(f"Year {year}:")
    
    # Inner loop for each month
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
        
        # Accumulate the total rainfall
        total_rainfall += rainfall
        total_months += 1

# Calculate the average rainfall per month
average_rainfall = total_rainfall / total_months

# Display the results
print(f"\nNumber of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
