#1. Write a Python program to read a CSV file and display its contents.

import csv

def read_csv(file_path):
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            row_count = 0
            for row in csv_reader:
                print(row)
                row_count += 1
                if row_count == 5:
                    break
    except FileNotFoundError:
        print(f"The file at path {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'aerofit_treadmill.csv'
read_csv(file_path)

'''
Output:

['Product', 'Age', 'Gender', 'Education', 'MaritalStatus', 'Usage', 'Fitness', 'Income', 'Miles']
['KP281', '18', 'Male', '14', 'Single', '3', '4', '29562', '112']
['KP281', '19', 'Male', '15', 'Single', '2', '3', '31836', '75']
['KP281', '19', 'Female', '14', 'Partnered', '4', '3', '30699', '66']
['KP281', '19', 'Male', '12', 'Single', '3', '3', '32973', '85']
'''


