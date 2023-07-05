# Import modules that will be used
import os
import csv

# Set the path for the CSV file
PyBankcsv = os.path.join("Resources","budget_data.csv")
# Set the path for the analysis file
PyBankAnalysis = os.path.join("Analysis","Analysis.txt")

# Create lists 
profit = []
monthly_changes = []
date = []

# Create variables
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Open the CSV variable PyBankcsv
with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Start loop and process file
    for row in csvreader:    
      # count months
      count = count + 1 

      # Set variable for greatest increase and decrease
      date.append(row[0])

      # calculate total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Check profit/loss and calculate the average 
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      #Create list for calculations
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      #Calculate the average 
      average_change_profits = (total_change_profits/count)
      
      #Find the min/max and dates 
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open(PyBankAnalysis, 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")