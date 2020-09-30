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
        number_months = number_months + 1

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

    # find the total sum of the profits/losses
        sum_profit_loss = sum(net_profit_loss)
        average_profit_loss = (sum_profit_loss/number_months)

     # find the largest profit and the largest loss
    largest_profit = max(profit_loss_changes)
    largest_loss = min(profit_loss_changes)

    # index the month with the highest profit and biggest loss
    largest_profit_index = profit_loss_changes.index(largest_profit)
    largest_loss_index = profit_loss_changes.index(largest_loss)

    # assign the biggest profit and biggest loss
    best_month = months[largest_profit_index]
    worst_month = months[largest_loss_index]

#Print
print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {number_months}')
print(f'Total: {net_profit_loss}')
print(f'Average Change: {average_profit_loss}')
print(f'Greatest Increase in Profit: {largest_profit}')
print(f'Greatest Loss in Profit: {largest_loss}')

budget_data_file = os.path.join ("budget_data.txt")
with open(budget_data_file, 'w') as outfile:

    outfile.write(f'Financial Analysis\n')
    outfile.write("--------------------\n")
    outfile.write(f'Total Months: {number_months}\n')
    outfile.write(f'Total: {net_profit_loss}\n')
    outfile.write(f'Average Change: {average_profit_loss}\n')
    outfile.write(f'Greatest Increase in Profit: {largest_profit}\n')
    outfile.write(f'Greatest Loss in Profit: {largest_loss}\n')