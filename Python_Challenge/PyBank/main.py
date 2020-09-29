import os
import csv

# set a path
csvpath = os.path.join("budget_data.csv")

# define variables
months = []
months_count = 0
net_profit= 0
month_profit= 0
month_change = 0
current_month_profit = 0
change = []

# open and read the csv file
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    csv_header = next(csv_file)

# Begin the loop to read through the rows
for row in csv_reader:

    # find the months in the data set
    months_count += 1

    net_profit += int(row[1])

    # calculate the profit
    month_profit = int(row[1])
    net_profit += current_month_profit

    # add each month to the list
    months.append(str(row[0]))

    # month to month change
    if change != 0:
        # set month value
        month_profit = int(row[1])

         # find the change in month's profit/loss
        change = month_change - change

         # add each month's profit to the list of changes
        change.append(month_change)

        change = int(row[1])
    elif change == 0:
        change = int(row[1])

# total profit change
sum_profit = sum(month_profit)
# average profit change
average_profit_loss = ((sum_profit/months -1), 2)

# Max change in profit
max_change = max(month_profit)

# Biggest loss in profit
min_change = min(month_profit)

# Idenitifying the month with highest profit
max_change_index = month_change.index(max_change)
min_change_index = month_change.index(min_change)

# Identify the best month
best_month = months[max_change_index]

# Identify the worst month
worst_month = months[min_change_index]

# Print Results
print(f'Financial Analysis')
print(f'------------------------')
print(f'Total Months: {months_count}')
print(f'Net Profit: {net_profit}')
print(f'Average Monthly Change: {month_change}')
print(f'Greatest increase in Profit: {max_change}')
print(f'Greatest loss in Profit: {min_change}')






