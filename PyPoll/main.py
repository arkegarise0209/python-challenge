#Dependencies
import os
import csv


#Join file paths based on user input for file selection
file_name = input("Please enter file name: ")
file = os.path.join("raw_data", file_name)

#define variables to track
total_votes = 0
candidate_options = []
election_stats = []
election_outcome = {}

#Read in csv file
with open(file, newline="") as election_data:
    csvreader = csv.reader(election_data, delimiter=",")
    next(csvreader, None)

#Loop through rows in data
    for row in csvreader:
    
     #Calculate total number of votes
        total_votes = total_votes + 1

    #Add candidates to list
        if row[2] not in candidate_options:
            candidate_options.append(row[2])
         
         #Add number of votes per candidate
            election_outcome[row[2]] = 1
            
        else:
            election_outcome[row[2]] = election_outcome[row[2]] + 1
    #Display output
    print()
    print("'''")
    print("Election Results")
    print("-----------------------------")
    print("Total Votes: " + str(total_votes))
    print("-----------------------------")

#Loop through dictionary for results of vote (candidate, percent of vote, number of votes)
    for candidate in election_outcome:
        election_results = (candidate + ": " + str(round(((election_outcome[candidate]/total_votes)*100))) + "%" + " (" + str(election_outcome[candidate]) + ")") 
        print(election_results)
        election_stats.append(election_results)
        
#Identify dictionary to parse
election_outcome

#Correlate winning amount of votes to winning candidate name
winner = max(election_outcome, key=election_outcome.get)

#Display output
print("-----------------------------")
print("Winner: " + str(winner))
print("-----------------------------")
print("'''")
print()


#Output files
output_file = os.path.join("election_results.txt")

with open(output_file, "w") as txt_file:
    
    txt_file.write("'''")
    txt_file.write("\n")
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-----------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes: " + str(total_votes))
    txt_file.write("\n")
    txt_file.write("-----------------------------")
    txt_file.write("\n")
    for row in election_stats:
        txt_file.write(str(row)+"\n")
    txt_file.write("-----------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner))
    txt_file.write("\n")
    txt_file.write("-----------------------------")
    txt_file.write("\n")
    txt_file.write("'''")
