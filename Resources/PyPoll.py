# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
#Declare a variable that holds an empty string value for the winning candidate
winning_candidate = ""
#Declare a variable for the "winning count" equal to zero
winning_count = 0
#Declare a variable for the "winning_percentage" equal to zero
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
#print(total_votes)

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        #candidate_options.append(candidate_name)

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
#print(candidate_options)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary.
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.

    #1. Use a for loop to iterate through the candidate_options = [] list. We will get the candidate's name
for candidate_name in candidate_votes:

    # 2. Use the for loop variable to retrieve the votes of the candidate from the candidate_votes = {} dictionary.
    votes = candidate_votes[candidate_name]

    # 3. Calculate the percentage of the vote count
    vote_percentage = float(votes) / float(total_votes) * 100

    # 4. Print each candidate and the percentage of votes using f-string formatting
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")