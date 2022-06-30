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
    """Writes a new CSV file created in the path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A CSV file containing the qualifying loans.

    """
    with open(new_csvpath, "w") as csvfile:
       # Create a csvwriter
        csvwriter = csv.writer(csvfile, delimiter=",")
        # Create Header
        header = ['Lender', 'Max Loan Amount', 'Max LTV' ,'Max DTI', 'Min Credit Score', 'Interest Rate']
        # Write the header to the CSV file
        csvwriter.writerow(header)

        # Write each list inside of `qualifying_loans`
        # as a row in the CSV file.
        for row in qualifying_loans:
            csvwriter.writerow(row)

