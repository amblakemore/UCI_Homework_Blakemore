import os
import csv

# set a path
csvpath = os.path.join("budget_data.csv")

# define variables
months = []
profit_loss_changes = []
number_months = 0 
net_profit_loss = 0
current_month_profit = 0
last_month_profit = 0
change_profit = 0

# open and read the csv file
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    csv_header = next(csv_file)

# Begin the loop to read through the rows
for row in csv_reader:

    # find the months in the data set
    number_months += 1

    # Total amount of the profit/loss
    current_month_profit = int(row[1])
    net_profit_loss += current_month_profit

    if (number_months ==1):
        # make the previous month the new current month
        last_month_profit = current_month_profit

    else:
        # calculate the change in profit/loss
        change_profit = current_month_profit - last_month_profit

        # add each month to our list
        months.append(row[0])

        # add each profit/loss to our list
        profit_loss_changes.append(profit_loss_changes)

        # make the current month the previous month to continue the loop
        last_month_profit = current_month_profit

    






