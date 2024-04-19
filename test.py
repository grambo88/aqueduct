import os
import csv
import pandas as pd
from time import sleep
import numpy as np 


def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def append_dataframes(new_info_df, entries_df, payouts_df):
    # Create an empty list to store the appended dataframes
    appended_dataframes = []

    # Append dataframes to the list
    appended_dataframes.append(new_info_df)
    appended_dataframes.append(entries_df)
    appended_dataframes.append(payouts_df)

    return appended_dataframes


def append_to_csv(df1, df2, df3, csv_filename):
    # Concatenate the DataFrames into a list
    concatenated_list = [df1, df2, df3]

    # Convert the list to a Pandas DataFrame
    concatenated_df = pd.concat(concatenated_list, axis=0, ignore_index=True)

    # Append the DataFrame to the CSV file
    concatenated_df.to_csv(csv_filename, mode='a', index=False, header=not pd.read_csv(csv_filename).shape[0])


def predict_output(matrix1, matrix2):
    # Ensure the input matrices have the correct shapes
    assert matrix1.shape == (7,) , "Matrix1 should be of shape 1 row x 7 columns"
    assert matrix2.shape == (16,7), "Matrix2 should be of shape 16 rows x 7 columns"

    # Perform some operation on the input matrices (you need to define the operation)
    # For example, let's concatenate the matrices and reshape to get a 4x4 matrix
    concatenated_matrix = np.concatenate((matrix1, matrix2), axis=0)
    predicted_matrix = np.reshape(concatenated_matrix[:4, :], (4, 4))

    return predicted_matrix


# Function to read CSV file and ensure 7 columns and 16 rows
def ensure_entries_csv_dimensions(filename):
    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Ensure 16 rows
    while len(rows) < 16:
        rows.append(['0'] * 7)
    
    # Ensure 7 columns
    for row in rows:
        while len(row) < 7:
            row.append('0')
        row = row[:7]  # Truncate if more than 7 columns
    
    # Write back to the CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Test the function
# ensure_csv_dimensions('your_csv_file.csv')

def ensure_payouts_csv_dimensions(filename):
    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Ensure 4 rows
    while len(rows) < 4:
        rows.append(['0'] * 7)
    
    # Ensure 4 columns
    for row in rows:
        while len(row) < 4:
            row.append('0')
        row = row[:4]  # Truncate if more than 4 columns
    
    # Write back to the CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def ensure_new_info_csv_dimensions(filename):
    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Ensure 1 rows
    while len(rows) < 1:
        rows.append(['0'] * 7)
    
    # Ensure 7 columns
    for row in rows:
        while len(row) < 7:
            row.append('0')
        row = row[:7]  # Truncate if more than 7 columns
    
    # Write back to the CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def horse_names_to_csv(filename):
    # Write back to the CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)



def process_files(folder_path):
    # List all files in the specified folder
    aqueduct_path = os.listdir(folder_path)
    # Loop through each file in the folder
    for date_dirs in aqueduct_path:

        # Construct the full path to the file
        date_path = os.path.join(str(folder_path), str(date_dirs))
        
        # print(date_path)
        race_list = os.listdir(date_path)
        # print(race_list)
        test_db = []

        for race_dirs in race_list:
            full_path = os.path.join(str(date_path), str(race_dirs))
            #print(full_path)

            test = os.listdir(full_path)
            entries = full_path + '\\' + 'entries.csv'
            new_info = full_path + '\\' + 'new_info.csv'
            payouts = full_path + '\\' + 'payouts.csv'

            file_paths = [entries, new_info, payouts]

            # Initialize an empty list to store datasets
            datasets = []

            #for file_path in file_paths:
            npa_new_info = np.genfromtxt(new_info, delimiter=',')
            npa_entries = np.genfromtxt(entries, delimiter=',', invalid_raise = False)
            npa_payouts = np.genfromtxt(payouts, delimiter=',')
            print('\n')
            print('the length of npa_new_info is: ',len(npa_new_info))
            print('the length of npa_entries is: ',len(npa_entries))
            print('the length of npa_payouts is: ',len(npa_payouts))
            print('\n')

            print('---- STARTING DIMENSION ENFORCEMENT ---- ')

            ensure_new_info_csv_dimensions(new_info)
            ensure_entries_csv_dimensions(entries)
            ensure_payouts_csv_dimensions(payouts)

            print('---- COMPLETED DIMENSION ENFORCEMENT ---- ')

            print('\n')
            print("NPA_NEW_INFO:")
            print(npa_new_info)
            print('\n')
            print('NPA_ENTRIES')
            print(npa_entries)
            print('\n')
            print('NPA_PAYOUTS')
            print(npa_payouts)
            print('\n')

            # predict_output(npa_new_info, npa_entries)

            print('success 1')
            print('Test Horse Names Only')
            print(npa_entries[:,1])
            
            print(len(npa_entries[:,1]))
            print('END')
            print('\n')

            # test = predict_output(npa_new_info, npa_entries)
            # print(test)

            test_db.append(npa_entries[:,1])
            # if npa_entries[:,1]
            # runner_list = npa_entries[:,1]
            print(test_db)
            for i in test_db:
                for x in i:
                    if x != 0:
                        print(x)
                    else:
                        pass

            sleep(1)

            # # Loop through each file path and read the CSV into a DataFrame, then append it to the list
            # for file_path in file_paths:
            #     df = pd.read_csv(file_path, header=None)
            #     datasets.append(df)
            # print(datasets)
            # print('\n')
            # print('success 2')
            # sleep(5)

            pass



# Specify the folder path you want to process
# folder_path = "/path/to/your/folder"

folder_path = "C:\\Users\\Tyler\\projects\\cybertooth-mod\\data\\aqueduct"
folder_path_test = "C:\\Users\\Tyler\\projects\\cybertooth-mod\\data\\aqueduct1"
# folder_path_test1 = "C:\\Users\\Tyler\\projects\\cybertooth-mod\\data\\aqueduct-test"
folder_path_test1 = "C:\\Users\\Tyler\\projects\\aqueduct\\data\\aqueduct-test"

# Call the function to process files in the folder
# process_files(folder_path)

process_files(folder_path_test1)


