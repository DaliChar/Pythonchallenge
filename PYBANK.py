
import os
import csv

# Reads in the CSVs for PyBank using Python 
# Successfully stores the header row

csvpath = os.path.join('budget_data.csv')
count=0
with open(csvpath,'r')as file:
       
    filecontent=csv.reader(file) 
    header=next(filecontent)
    print(header)


    for row in filecontent: 
        print(row[0])
       
        count=count+1
        
    print(count) 
        

# #### Create a Python script that analyzes the records to calculate each of the following
# 
# - The total number of months included in the dataset 
# 
# - The net total amount of "Profit/Losses" over the entire period
# 
# - The changes in "Profit/Losses" over the entire period, and then the average of those changes

#creating somewhere to store the data



total_months=[]
profit_losses = []
monthly_changes = []
overall_profit = 0
total_change_profits = 0
initial_profit = 0



# Will need it when collecting the greatest increase and decrease in profits
total_months.append(row[0])
profit_losses.append(row[1])
overall_profit = overall_profit + int(row[1])





# Append the profit information & calculate the total profit
profit_losses.append(row[1])
overall_profit = overall_profit + int(row[1])




final_profit = int(row[1])
monthly_change_profits = final_profit - initial_profit





#Store these monthly changes in a list
monthly_changes.append(monthly_change_profits)





total_change_profits = total_change_profits + monthly_change_profits
initial_profit = final_profit




#Calculate the average change in profits
change_profit_losses_on_average = (total_change_profits/count)





greatest_increase_profits = max(monthly_changes)
greatest_decrease_profits = min(monthly_changes)





increase_date = total_months[monthly_changes.index(greatest_increase_profits)]
decrease_date = total_months[monthly_changes.index(greatest_decrease_profits)]





print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total: " + "$" + str(overall_profit))
print("Average Change: " + "$" + str(int(change_profit_losses_on_average)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
print("----------------------------------------------------------")




with open('PyBank Analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total: " + "$" + str(overall_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(change_profit_losses_on_average)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")








