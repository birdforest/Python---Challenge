# Import the OS and CSV Module
import os
import csv

# Set the path for the CSV file containing budget data
csvpath = os.path.join("Resources", "budget_data.csv")

# Define the variables and store the total month, net total, and lists to contain # of months, profit/loss monthly changes, greatest profit/loss increase/loss
total_month = 0
net_total = 0
average_change = 0
month = []
monthly_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row (since it is not going to be a returned value)
    next(csvreader)
    # Run through each row with the iteration
    for row in csvreader:
        # Increment the total month count
        total_month = total_month + 1
        # Calculate the net total profit/loss
        net_total = net_total + int(row[1])
        # Store # of months and monthly profit/loss values in each list
        month.append(row[0])
        monthly_change.append(int(row[1]))
    
        # The loop will iterate from 1 up to the length of the "monthly_change" list
        for i in range(1, len(monthly_change)):
            # profit/loss change is calculated by subtracting the current month's value from the previous month's value
            change = monthly_change[i] - monthly_change[i-1]
            
            # Condition used to calculate the greatest increase and decrease
            # If the current 'change' value is greater than the value stored in 'greatest_increase[1]' list, it updates both 'greatest_increase[1]' and 'greatest_increase[0]' with the current 'change' value and the corresponding month
            # Vice Versa with the greatest decrease scenario
            if change > greatest_increase[1]:
                greatest_increase[1] = change
                greatest_increase[0] = month[i]
            if change < greatest_decrease[1]:
                greatest_decrease[1] = change
                greatest_decrease[0] = month[i]

        # Define the variable and store the total change to calculate the average change in changes in "Profit/Losses"
        total_change = 0

        for i in range(1, len(monthly_change)):
            # Calculate the total change by adding the difference between the profit/loss of the current month and that of the previous month to the total
            total_change = total_change + (monthly_change[i]) - (monthly_change[i-1])
            # Calculate average change by divided the total change from the number of changes
            average_change = total_change/(len(monthly_change)-1)
            # Format the average change so the result contains 2 decimal places
            formatted_average_change = format(average_change, '.2f')


# The print functions are based on the questions assigned
# F-strings are created to replace the value of the corresponding variables
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${net_total}")
print(f"Average Change: ${formatted_average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
