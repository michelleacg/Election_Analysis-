#We can use a for loop to iterate over a dictionary and get all the keys, all the values, or all the keys and values
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#To get only the keys from a dictionary using a for loop, the loop can be written like we are iterating over a list or tuple.
for county in counties_dict:
    
    print(county)

#keys()method to iterate over a dictionary to get the keys

for county in counties_dict.keys():
    
    print(county)

#To get the values of a dictionary, we iterate over the dictionary using the values() method, just like we used the keys() method.

for voters in counties_dict.values():

    print(voters)

for county in counties_dict:

    print(counties_dict[county])

for county in counties_dict:

    print(counties_dict.get(county))

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    
    print(county_dict)

for county_dict in voting_data:

    for value in county_dict.values():

        print(value)

for county_dict in voting_data:

    print(county_dict['county'])


my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#using concatenade
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#And here's how you would edit the code to use f-strings
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#Here's the counties dictionary and the solution for that Skill Drill if we use concatenation
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#If we use f-stings, we can rewrite the print statement to be more intuitive and clear
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multiline F-Strings

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

#Format Floating-Point Decimals
#f'{value:{width}.{precision}}'


#Multiline F-Strings with Format Floating-Point Decimals

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")