#Dependencies
import os
import csv

#Join file paths based on selected csv file
file_name = input("Please enter file name: ")
file = os.path.join("raw_data", file_name)

#Define variables
emp_ID = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

#State abbreviations dictionary 
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Read in needed csv file
with open(file, newline="") as employee_info:
    csvreader = csv.reader(employee_info, delimiter=",")
    next(csvreader, None)

#Loop through rows of data
    for row in csvreader:

    #Add each employee ID to emp_ID list
        emp_ID.append((row[0]))

    #Add first name to first_name list
        first_name.append(row[1].split(" ")[0])

    #Add last name to last_name list
        last_name.append(row[1].split(" ")[1])

    #Reformat DOB and add to dob list
        dob.append(row[2].split("-")[1] + "/" + row[2].split("-")[2] + "/" + row[2].split("-")[0])

    #Reformat SSN and add to ssn list
        ssn.append("***-**-" + row[3].split("-")[2])

    #Abbreviate State and add to state list
        state.append(us_state_abbrev[row[4]])

#Zip lists together to make one dataset 
clean_employee_records = zip(emp_ID,first_name,last_name,dob,ssn,state)

#Output new file
clean_data_file = os.path.join("employee_info.csv")

with open(clean_data_file, "w" ,newline="") as csvfile:
    clean_csv = csv.writer(csvfile, delimiter=",")
    clean_csv.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    clean_csv.writerows(clean_employee_records)








