# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.

### Task assignment
1. Total number of votes cast.
2. A complete list of candidates who received votes.
3. Total number of votes each candidate won.
4. Percentage of votes each candidate won.
5. The winner of the election based on popular vote.
6. The voter turnout for each county.
7. The percentage of votes from each county out of the total count.
8. The county with the highest turnout.

## Resorurces
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.63.1


## Election-Audit Results: 

![Election Audit Results screenshot from Terminal](Resources/PyPoll_Challenge_Results_Terminal.PNG)

![Election Audit Results screenshot from Text file](Resources/PyPoll_Challenge_Results_Textfile.PNG)

### Election-Audit Summary: 
    
The **total votes** cast in this congressional district is 369,711. Across the three counties - Jefferson, Denver and Arapahoe, Denver had the highest turnout accounting for 82.8% of the total votes cast. Below is the County votes summary.

**COUNTY VOTES SUMMARY:**
1. Jefferson: 10.5% (38,855)
2. Denver: 82.8% (306,055)
3. Arapahoe: 6.7% (24,801)

The **winner** for this congressional district is Diana DeGette with the vote count of 272,892 which is 73.8% of total votes. Below is the final vote count for each candidate.   -------------------------
**FINAL CANDIDATE VOTE COUNT:**
1. Charles Casper Stockham: 23.0% (85,213)
2. Diana DeGette: 73.8% (272,892)
3. Raymon Anthony Doane: 3.1% (11,606)

The script written for doing the above audit can be for:
1. Other congressional district elections.
    - Include the data about congressional district (unique identifier) in the source data file.
    - Update the script to introducing variables to capture the Congresstional district ID.
        ```python
        # Track Congressional district
        congressional_district = []
        
        # For each row in the CSV file.
        for row in reader:
            # Get the Congressional district from each row.
            congressional_district = row[4]
        ```

    - In the output, print the Congresstional district ID in the Election Results.
        ```python
        # Print the final vote count (to terminal)
        election_results = (
            f"\nElection Results for {congressional_district}\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
            f"COUNTY VOTES:\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)  
        ```
        
2. Senetorial elections 
    - by removing the county votes section as senetorial elections are at state level.
       ```python
       # Write an if statement to determine the winning county and get its vote count.
        if (county_vote > highest_county_vote) and (county_percentage > highest_county_percentage):
            highest_county_vote = county_vote
            highest_county_turnout = county_name
            highest_county_percentage = county_percentage
        # Print the county with the largest turnout to the terminal.
        highest_county_turnout_summary = (
            f"\n-------------------------\n"
            f"HIGHEST TURNOUT COUNTY SUMMARY:\n"
            f"County: {highest_county_turnout}\n"
            f"Vote count: {highest_county_vote:,}\n"
            f"Vote percentage: {highest_county_percentage:.1f}%\n"
            f"\n-------------------------\n")
        print(highest_county_turnout_summary)
        # Save the county with the largest turnout to a text file.
        txt_file.write(highest_county_turnout_summary)
        ```

3. Primary elections to determine candidates for general elections from each party by adding code to capture the party.
    - The data source file needs to have Party information
4. Local elections with little customization.


