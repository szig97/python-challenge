#1. Import the modules
import os
import csv

#2. Set csv path
pybankcsv = os.path.join("Resources", "budget_data.csv")

#3. Set initial variables
count = 0
net_profit_loss = 0
current_month_profit_loss = 0
previous_month_profit_loss = 0
profit_loss_change = 0

#4. Create lists to store data
profit_loss_changes = []
date = []

#5. Open the csv
with open(pybankcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #6. Count the total number of months included in the dataset 
        count += 1

        #7. Calculate the net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count == 1):
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            date.append(row[0])
            profit_loss_changes.append(profit_loss_change)
            previous_month_profit_loss = current_month_profit_loss

        #8. Calculate the changes in "Profit/Losses" over the entire period
        total_profit_loss = sum(profit_loss_changes)
        average_profit_loss = round(total_profit_loss/(count - 1), 2)

        #9. Find the greatest increase in profits (date and amount) over the entire period
        highest_change = max(profit_loss_changes)
        highest_month_index = profit_loss_changes.index(highest_change)
        increase_date = date[highest_month_index]
       
        #10. Find the greatest decreases in profits (date and amount) over the entire period
        lowest_change = min(profit_loss_changes)
        lowest_month_index = profit_loss_changes.index(lowest_change)
        decrease_date = date[lowest_month_index]

    #11. Print the data
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${net_profit_loss}")
    print(f"Average Change: ${average_profit_loss}")
    print(f"Greatest Increase in Profits: {increase_date} (${highest_change})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${lowest_change})")

#12. Export the data to a text file
financial_analysis = os.path.join("Analysis", "financial_analysis.txt")
with open(financial_analysis, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("--------------------------------------------------------\n")
    outfile.write(f"Total Months: {count}\n")
    outfile.write(f"Total: ${net_profit_loss}\n")
    outfile.write(f"Average Change: ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits: {increase_date} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Profits: {decrease_date} (${lowest_change})\n")



