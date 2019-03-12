import os
import csv
budget_data = '.\budget_data.csv'
total_months = 0
total_amount = 0
profit = []
time = []
profitChange = 0


with open(budget_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    for row in csvreader:
        total_months = total_months + 1
        total_amount = total_amount + int(row[1])
        profit.append(int(row[1]))
        time.append(row[0])
average = round(total_amount/total_months, 2)
a = profit.index(max(profit))
b = profit.index(min(profit))
output = (
     "Financial Analysis\n"
     "----------------------------\n"
     f"Total Months: {total_months}\n"
     f"Total: ${total_amount}\n"
     f"Average Change: ${average}\n"
     f"Greatest Increase in Profit: {time[a]}  $({max(profit)})\n"
     f"Greatest Decrease in Profit: {time[b]}  $({min(profit)})")

# Print the output (to terminal)
print(output)
output_file = os.path.join('new_file.txt')
# Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
