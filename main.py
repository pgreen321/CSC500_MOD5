# Part 1: A program that uses nested loops to collect data and calculate the average rainfall over a period of years.

rainfall = {'January': [], 'February': [], 'March': [], 'April': [], 'May': [], 'June': [], 'July': [],
            'August': [], 'September': [], 'October': [], 'November': [], 'December': []}

# The program should first ask for the number of years
num_years = int(input("Enter number of years to add rainfall data: "))

# Outer loop will iterate once for each year
for n in range(num_years):
    # Inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for
    # the inches of rainfall for that month.
    for month in rainfall:
        year = n + 1
        amount_rainfall = float(input('Enter amount of rainfall in {} in inches for year {}: '.format(month, year)))
        rainfall[month].append(amount_rainfall)

# After all iterations, the program should display the number of months, the total inches of rainfall, and the average
# rainfall per month for the entire period.

total_months = 0
total_inches = 0
for month in rainfall:
    total_months += len(rainfall[month])
    total_inches += sum(rainfall[month])
total_average = float(total_inches / total_months)

print()
print('There are {} months in the {} year period'.format(total_months, num_years))
print('The total amount of rain that fell in the {} year period was {} inches'.format(num_years, total_inches))
print('The average monthly rainfall over the {} year period was {:.2f} inches'.format(num_years, total_average))
print('The average rainfall for each month over the {} year period was:'.format(num_years))

for month in rainfall:
    rainfall_month = sum(rainfall[month])
    avg_rainfall_month = rainfall_month / len(rainfall[month])
    print('{} : {:.2f} inches'.format(month, avg_rainfall_month))

# Part 2: This program calculates the number of points a user has earned based on how many books they have purchased

# Ask user to enter the number of books they purchased this month
books_purchased = int(input('How many books do you purchase this month?\n'))

# Determine number of points to award
if books_purchased == 0 or books_purchased == 1:
    points = 0
elif books_purchased == 2 or books_purchased == 3:
    points = 5
elif books_purchased == 4 or books_purchased == 5:
    points = 15
elif books_purchased == 6 or books_purchased == 7:
    points = 30
elif books_purchased >= 8:
    points = 60
else:
    points = 0

# Tell user how many points they have been awarded
print('You purchased {} books and have been awarded {} points.'.format(books_purchased, points))