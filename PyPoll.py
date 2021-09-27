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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
   



# Using the open() function with the "w" mode we will write data to the file.
## outfile = open(file_to_save, "w")

# Write some data to the file.
##outfile.write("Hello World")

# Close the file
##outfile.close()

#Using the with statement open the file as a text file.
##with open(file_to_save, "w") as txt_file:
      # Write three counties to the file.
     ##txt_file.write("Counties in the Election\n-------------------------------\nArapahoe\nDenver\nJefferson")
