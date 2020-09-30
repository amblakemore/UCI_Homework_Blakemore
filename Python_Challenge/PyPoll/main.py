import os
import csv

# Set the variables
candidates = []
number_votes = 0
vote_counts = []
election_data = ['1', '2']

# Create a path to our csv file in the same folder
election_dataCSV = os.path.join("election_data.csv")

    # Read through the file
with open(election_dataCSV) as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    csv_header = next(csv_file)
        
    # Start the loop
    for line in csvreader:

     # Vote Count
        number_votes = number_votes + 1

    # Name the Canditates
    candidate = line[2]

    # Tally the votes
    if candidate in candidates:
        candidate_index = candidates.index(candidate)
        vote_counts[candidate_index] = vote_counts[candidate_index] + 1

    else:
        candidates.append(candidate)
        vote_counts.append(1)

# Declare additional variables
percentages = []
max_votes = vote_counts[0]
max_index = 0

# Determine the winner 
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/number_votes * 100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]
percentages = [round(i, 2) for i in percentages]

# Print the Results
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {number_votes}')
print(f'-------------------------')
for count in range(len(candidates)):
    print(f'{candidates[count]}: {percentages[count]}% ({vote_counts[count]})')
print(f'-------------------------')
print(f'Winner: {winner}')

# # Export
# output_file = election_dataCSV[0:-4]
# write_election_dataCSV = f'{output_file}pypoll_results.txt'
# filewriter = open(write_election_dataCSV, mode = "w")

# # Text File
# filewriter.write('Election Results')
# frilewriter.write('-------------------------')
# filewriter.write('Total Votes: {number_votes}')
# filewriter.write('-------------------------')
# for cocunt in range(len(candidates)):
#     filewriter.write('{candidates[count]}: {percentages[count]}% ({vote_counts[count]})')
# filewriter.write('-------------------------')
# filewriter.write('Winner: {winner}')


            
