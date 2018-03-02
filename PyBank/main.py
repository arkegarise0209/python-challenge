import os
import csv

#Need help understanding what needs to be in () to join paths on os
budget_data_1_csv = os.path.join("..","PyBank","raw_data","budget_data_1.csv")

#define variables to track
total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0

monthly_revenue_changes = []

#Read in the needed csv file
with open(budget_data_1_csv, newline="") as revenue_data:
    csvreader = csv.reader(revenue_data, delimiter=",")

#Loop through rows of data
for row in csvreader:

    #Calculate month and revenue totals
    total_months = total_months + 1

    total_revenue = total_revenue + int(row["Revenue"]) 
    
    #Track monthly change in revenue
    revenue_change = int(row["Revenue"] - prev_revenue)

    #Update value of prev_revenue for next loop
    prev_revenue = int(row["Revenue"])

    #Greatest increase in revenue


    #Greatest decrease in revenue



    #Add monthly change in revenue to monthly_revenue_changes list 
    monthly_revenue_changes.append(int(revenue_change))

#Calculate average change in monthly revenue
average_monthly_change = sum(monthly_revenue_changes) / len(monthly_revenue_changes)





#display output
print()
print()
print("Financial Analysis")
print("-------------------")
print("Total Months:"+ " " + str(total_months))
print("Total Revenue:" + " " + "$" + str(total_revenue))
print("Average Revenue Change:" + " " + str(average_monthly_change))
print("Greatest Increase in Revenue:" + " " + str(greatest_increase))
print("Greatest Decrease in Revenue:" + " " + str(greatest_decrease))
print("-------------------")
print()
