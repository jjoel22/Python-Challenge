# Modules
import os
import csv

# The total number of months included in the dataset
month_list = []
# The net total amount of "Profit/Losses" over the entire period
net_amount = []
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
profit_losses = []
# The month for net change
profit_losses_month = []
# The greatest increase in profits (date and amount) over the entire period
greatest_increase = ["", 0]
# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = ["", 99999999999999999]
# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header_row = next(csvreader)

    # Extract first row (month) for computation of change
    first_row = next(csvreader)
    month_list.append(first_row[0])
    net_amount.append(int(first_row[1]))
    previous_profit_loss = int(first_row[1])
    
    # Loop through looking for the video
    for row in csvreader:
        # Tracking totals
        month_list.append(row[0])
        net_amount.append(int(row[1]))

        ## Tracking net changes
        # Current month's profit_loss
        current_profit_loss = int(row[1])

        # Current month's change using previous month's profit_loss
        change = current_profit_loss - previous_profit_loss

        # Update previous_profit_loss with current month's proft_loss for next iteration
        previous_profit_loss = current_profit_loss

        # Store current's months profit_loss
        profit_losses.append(change)

        # Acquire month for which profit_loss occurred
        profit_losses_month.append(row[0])

        # Compute greatest increase
        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change

        # Compute greatest decrease
        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change

net_monthly_avg = sum(profit_losses) / len(profit_losses)

text_out = (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {len(month_list)}\n"
f"Total: ${sum(net_amount)}\n"
f"Average Change: ${net_monthly_avg:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
)

print(text_out)

out_path = os.path.join("analysis", "budget_analysis.txt")

with open(out_path, "w") as txtfile:
    txtfile.write(text_out)
