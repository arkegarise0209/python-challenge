#Dependencies
import os
import csv
from operator import itemgetter
from collections import OrderedDict

#Join file paths
election_data_1_csv = os.path.join("..","..","UNCCHAR201802DATA2-Class-Repository-DATA", "Homework", "Week-03-Python", "Instructions", "PyPoll", "raw_data", "election_data_1.csv")

#define variables to track
total_votes = 0
candidates = []
outcome = {}

#Read in the needed csv file
with open(election_data_1_csv, newline="") as election_data:
    csvreader = csv.reader(election_data, delimiter=",")


#Loop through rows in data
    for row in csvreader:

    #Calculate total number of votes
        total_votes = total_votes + 1
        
    #Create list of candidates  
        if row["Candidate"] not in candidates:
            candidates.append(row["Candidate"])
         
         #Add number of votes per candidate
            outcome[row["Candidate"]] = 1
            
        else:
            outcome[row["Candidate"]] = outcome[row["Candidate"]] + 1


#Results of vote (candidate, percent of vote, number of votes)
    for candidate in outcome:
        candidate_results = (candidate + str(round(((outcome[candidate]/total_votes)*100))) + str(outcome[candidate]))

outcome

winner = sorted(outcome.item(), key=itemgetter(0), reverse=True)

#Display output
print()
print("Election Results")
print("-----------------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------------")
print(str(candidate) + ": " + str(round(outcome(row[2]) / str(total_votes))*100) + "% " + "(" + str(outcome(row[2] + ")")))
print("-----------------------------")
print("Winner: " + str(winner[0]))
print("-----------------------------")
print()


#Output files
output_file = os.path.join("..","election_results_1.txt_file")

with open(file_to_output, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write
    txt_file.write
    txt_file.write
    txt_file.write
    txt_file.write
    txt_file.write
    txt_file.write
    