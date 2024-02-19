# Import the OS and CSV Module
import os
import csv

# Set the path for the CSV file containing election data
csvpath = os.path.join("Resources", "election_data.csv")

# Define the variables and store the total votes, different candidates, and votes per candidate
# The reason for choosing set over list for 'candidates' is because duplicate elements are not preferred in this exercise
total_votes = 0
candidates = set()
candidate_votes = {}

# Read the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row (since it is not going to be a returned value)
    next(csvreader)
    # Run through each row with the iteration
    for row in csvreader:
        # Increment the total vote count
        total_votes = total_votes + 1
        # Obtain the candidate name from the row
        candidate = row[2]
        # Add unique candidate names to the set (the add() function does nothing if the element is already present in the set)
        candidates.add(candidate)
        # Retrieve the current vote count for 'candidate' from the candidate_votes' dictionary
        # If the candidate is not already in the dictionary, 'get()' returns '0' as a default value
        # Increment vote count by 1 which adds one more vote to the corresponding candidate
        # Store back in the 'candidate_votes' dictionary under the key 'candidate'
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

# The print functions are based on the questions assigned
# F-strings are created to replace the value of the corresponding variables
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Run through each candidate and their corresponding votes in the 'candidate_votes' dictionary
for candidate, each_votes in candidate_votes.items():
    # Calculate the percentage of votes each candidate won
    percentage = (each_votes / total_votes) * 100
    # Print candidate name, percentage of votes to 3 decimal points, and the total number of votes won per candidate
    print(f"{candidate}: {percentage: .3f}% ({each_votes})")

print("-------------------------")
# Obtain the maximum number of votes to determine the winner
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("-------------------------")