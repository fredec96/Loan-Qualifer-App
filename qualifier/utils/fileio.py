# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(new_csvpath,qualifying_loans):
    """Saves the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A 

    """
    with open(new_csvpath, "w") as csvfile:
       # Create a csvwriter
        csvwriter = csv.writer(csvfile, delimiter=",")
        # Create Header
        header = ['Lender', 'Max Loan Amount', 'Max LTV' ,'Max DTI', 'Min Credit Score', 'Interest Rate']
        # Write the header to the CSV file
        csvwriter.writerow(header)

        # Write the values of each dictionary inside of `qualifying_loans`
        # as a row in the CSV file.
        for item in qualifying_loans:
            csvwriter.writerow(item.values())



# Create a Path to a new CSV file
#csvpath = Path("large_equity_rounds.csv")

# Open the output CSV file path using `with open`
#with open(csvpath, "w") as csvfile:
    # Create a csvwriter
    #csvwriter = csv.writer(csvfile, delimiter=",")

    # Write the header to the CSV file
    #csvwriter.writerow(header)

    # Write the values of each dictionary inside of `big_raisers`
    # as a row in the CSV file.
    #for item in bank_data_filtered:
        #csvwriter.writerow(item.values())