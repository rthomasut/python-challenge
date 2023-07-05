# Import modules that will be used
import os
import csv

# Set the path for the CSV file
PyPollcsv = os.path.join("Resources","election_data.csv")
# Set the path for the analysis file
PyPollAnalysis = os.path.join("Analysis","Analysis.txt")

# Create lists 
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV variable PyPollcsv
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # Start loop and process file
    for row in csvreader:
        # Count votes
        count = count + 1
        # Assign names to candidatelist
        candidatelist.append(row[2])
        # Get unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # total votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # percent votes
        z = round((y/count)*100, 2)
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Create output file and place in the Analysis folder

with open(PyPollAnalysis, 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
