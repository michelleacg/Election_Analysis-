# Election_Analysis-

#An Analysis of Kickstarter Campaigns

## Project Overview 

A Colorado Board of Elections employee has given you the following tass to complete the election audit of a recent local congressional election.

  1. Calculate the total number of votes cast.
  2. Get a complete list of candidates who received votes.
  3. Calculate the total number of votes each candidate received.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on popular vote.

The purpose of the Kickstarter Analysis is to help Louise make informed decisions for her theater campaign fundraising by analyzing historical data to find trends from the crowdfunding platform Kickstarter, where project creators add incentives for different pledge amounts. 

## Resources

- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.71.2


## Summary

The analysis of the election show that:

  - There were 369,711 votes cast in the election.
  - The candidates were:
     -  Charles Casper Stockham
     -  Diana DeGette
     -  Raymon Anthony Doane
  - The candidates results were:
     -  Charles Casper Stockham received 23.0% of the vote and 85,213 votes
     -  Diana DeGette received 73.8% of the vote and 272,892 votes
     -  Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
  - The winner of the election was: 
     - Diana DeGette received 73.8% of the vote and 272,892 votes

## Challenge Overview

## Challenge Summary


## Overview of Election Audit: 

The purpose of this election audit analysis is to help Seth and Tom, member of the board of elections to audit a US Congressional precinct in Colorado. The task is to report the total of votes, the total of votes per candidate, the percentage of votes each candidate received, and the winner of the election based on the popular vote. Once this code is proofed to work, it will be used in other Senatorial Discticts and Local Elections. 

## Election-Audit Results: 

Election Outcomes:

- Votes cast in this congressional election were 369,711

- County Votes:

  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)

- The county with the largest number of votes was Denver

- Breakdown of the number of votes and the percentage of the total votes each candidate received:

  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
  
- Election winner:

  - Winner: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%

# **Code:**

#-*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

#Add our dependencies.
import csv
import os

#Add a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
#Add a variable to save the file to a path.
file_to_save = os.path.join("election_results.txt")

#Initialize a total vote counter.
total_votes = 0

#Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

#1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

#Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#2: Track the largest county and county voter turnout.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

#Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


#Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_options:

        # 6b: Retrieve the county vote count.
        county_vote = county_votes[county]

        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(county_vote) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county}: {county_vote_percentage:.1f}% ({county_vote:,})\n")

        print (county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_vote > winning_county_count) and (county_vote_percentage > winning_county_percentage):
            winning_county_count = county_vote
            winning_county_percentage = county_vote_percentage
            winning_county = county

    # 7: Print the county with the largest turnout to the terminal.
        winning_county_print = (
            f"-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n")
    print(winning_county_print)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_print)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

    #TheEnd

## Election-Audit Summary: 

In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
