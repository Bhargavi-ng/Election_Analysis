# Assignment Tasks: Data that needs to be retrieved.
# 1. Total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. Total number of votes each candidate won.
# 4. Percentage of votes each candidate won.
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Declare a new list for candidates.
candidate_options = []
# Declare a dictionary for candidate and votes.
candidate_votes = {}
# Declare Winning candidate and Winning count tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    #Print each row in the csv file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Initialize candidate's vote count to zero.
            candidate_votes[candidate_name] = 0

        # Add to that candidate's vote count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Save each candidate's name, vote count, and percentage of votes in a variable.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print to terminal
        print(candidate_results)
        # Save to text file.
        txt_file.write(candidate_results)


        # Determine winning vote count, winning percentage and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes, winning_percent = vote_percentage and winning_candidate= candidate's name.
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # print the winning summary.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    # Save to text file.
    txt_file.write(winning_candidate_summary)
            

        # Print the total votes.
        #print(f'The total number votes cast {total_votes:,}.\n')

        # Print the candidate list.
        #print(f'The list of candidates are {candidate_options}.')

        # Print each candidate's vote count.
        #for candidate_name, votes in candidate_votes.items():
            #print(f'{candidate_name} has received {votes:,}.')

        # Print percentage of votes each candidate received.
        #for candidate_name, votes in candidate_votes.items():
            #print(f'{candidate_name} received {votes/total_votes*100 :.1f}% of total votes.')





