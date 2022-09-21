# # # DATE AND TIME DEPENDENCIES
# # # # Import the datetime class from the datetime module.
# # # import datetime
# # # # Use the now() attribute on the datetime class to get the present time.
# # # now = datetime.datetime.now()
# # # # Print the present time.
# # # print("The time right now is ", now)

# # # # Import the datetime class from the datetime module.
# # # import datetime as dt
# # # # Use the now() attribute on the datetime class to get the present time.
# # # now = dt.datetime.now()
# # # # Print the present time.
# # # print("The time right now is ", now)


# # #dir(csv)
# # #['Dialect', 'DictReader', 'DictWriter', 'Error', 'OrderedDict', 'QUOTE_ALL', 'QUOTE_MINIMAL', 'QUOTE_NONE', 'QUOTE_NONNUMERIC', 'Sniffer', 'StringIO', '_Dialect', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'excel', 'excel_tab', 'field_size_limit', 'get_dialect', 'list_dialects', 're', 'reader', 'register_dialect', 'unix_dialect', 'unregister_dialect', 'writer']

# # # Total number of votes cast
# # # A complete list of candidates who received votes
# # # Total number of votes each candidate received
# # # Percentage of votes each candidate won
# # # # The winner of the election based on popular vote.

# # import csv
# # import os

# # # Assign a variable for the file to load and the path.
# # file_to_load = os.path.join ("Resources","election_results.csv")

# # # Open the election results and read the file.
# # with open(file_to_load) as election_data:

# #     # Print the file object.
# #      print(election_data)

# # Add our dependencies.
import csv
import os

# # Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# # Open the election results and read the file.
#with open(file_to_load) as election_data:

#     # Print the file object.
#     #  print(election_data)

#     # To do: read and analyze the data here.

#     #reader = csv.reader(election_data)

# # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# # # Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")

# # # Write some data to the file.
# # outfile.write("Hello World")

# # # Close the file
# outfile.close()

# # # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
   # txt_file.write("Counties in the Election\n------------------------------\nArapahoe\nDenver\nJefferson")

# # Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here

    # Read the file object with the reader function.

    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    
    #for row in file_reader:
    
    #    print(row)

            # Print the header row.
    
    # Read and print the header row.

    headers = next(file_reader)
    
    print(headers)