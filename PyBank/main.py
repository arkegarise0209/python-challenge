#Dependencies
import os
import csv


#Join file paths based on user input for file selection
file_name = input("Please enter file name: ")
file = os.path.join("raw_data", file_name)

#define variables to track
total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0

monthly_revenue_changes = []

greatest_increase = ["",0]
greatest_decrease = ["",9999999999999]

#Read in the needed csv file
with open(file, newline="") as revenue_data:
    csvreader = csv.reader(revenue_data, delimiter=",")
    next(csvreader, None)
#Loop through rows of data
    for row in csvreader:
        
    #Calculate month and revenue totals
        total_months = total_months + 1
        
        
        total_revenue = total_revenue + int(row[1])        
        
    #Track monthly change in revenue
        revenue_change = int(row[1]) - prev_revenue

    #Update value of prev_revenue for next loop
        prev_revenue = int(row[1])
    
    #Greatest increase in revenue
        if revenue_change > greatest_increase[1]:
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row[0]
     
    #Greatest decrease in revenue
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row[0]
    
    #Add monthly change in revenue to monthly_revenue_changes list 
        monthly_revenue_changes.append(int(revenue_change))

#Calculate average change in monthly revenue
    average_monthly_change = sum(monthly_revenue_changes) / len(monthly_revenue_changes)




#Display output
print("'''")
print("Financial Analysis")
print("----------------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + "$" + str(total_revenue))
print("Average Revenue Change: " + "$" + str(int(average_monthly_change)))
print("Greatest Increase in Revenue: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
print("Greatest Decrease in Revenue: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
print("'''")
print()


#Output files
output_file = os.path.join("budget_data_analysis.txt")

with open(output_file, "w", newline="") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("--------------------------------------------------------")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(average_monthly_change))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")