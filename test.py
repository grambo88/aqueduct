import os
import csv
import pandas as pd
from time import sleep
import numpy as np 

filename = 'data.csv'
filename1 = 'data1.csv'
filename2 = 'data2.csv'
filename3 = 'data3.csv'

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
    assert matrix1.shape == (6,) , "Matrix1 should be of shape (1, 6)"
    assert matrix2.shape == (16,6), "Matrix2 should be of shape (16, 6)"

    # Perform some operation on the input matrices (you need to define the operation)
    # For example, let's concatenate the matrices and reshape to get a 4x4 matrix
    concatenated_matrix = np.concatenate((matrix1, matrix2), axis=0)
    predicted_matrix = np.reshape(concatenated_matrix[:4, :], (4, 4))

    return predicted_matrix


def process_files(folder_path):
    # List all files in the specified folder
    aqueduct_path = os.listdir(folder_path)

    filename = 'data.csv'
    filename1 = 'data1.csv'
    filename2 = 'data2.csv'
    filename3 = 'data3.csv'


    # Loop through each file in the folder
    for date_dirs in aqueduct_path:

        # Construct the full path to the file
        date_path = os.path.join(str(folder_path), str(date_dirs))
        
        # print(date_path)
        race_list = os.listdir(date_path)
        # print(race_list)

        for race_dirs in race_list:
            full_path = os.path.join(str(date_path), str(race_dirs))
            #print(full_path)

            test = os.listdir(full_path)
            entries = full_path + '\\' + 'entries.csv'
            new_info = full_path + '\\' + 'new_info.csv'
            payouts = full_path + '\\' + 'payouts.csv'

            # entries_df = pd.read_csv(entries, sep=',', header=None)
            # new_info_df = pd.read_csv(new_info, sep=',', header=None)
            # payouts_df = pd.read_csv(payouts, sep=',', header=None)


            #print(entries_df.values)
            #    print(entries_df, new_info_df, payouts_df)
            # Trying to add '0,0,0,0,0,0' to the entries files that do not have 16 rows

            file_paths = [entries, new_info, payouts]

            # Initialize an empty list to store datasets
            datasets = []
            mod_dataset = []

            #for file_path in file_paths:

            npa_new_info = np.genfromtxt(new_info, delimiter=',')
            npa_entries = np.genfromtxt(entries, delimiter=',')
            npa_payouts = np.genfromtxt(payouts, delimiter=',')


            mod_dataset.append(npa_new_info)
            mod_dataset.append(npa_entries)
            mod_dataset.append(npa_payouts)

            print(npa_new_info.shape)
            print(npa_entries.shape)

            print('\n')
            print(npa_new_info)
            print('\n')
            print(npa_entries)
            print('\n')

            # predict_output(npa_new_info, npa_entries)


            print(mod_dataset)
            print('\n')
            print('success 1')
            sleep(5)

            # Loop through each file path and read the CSV into a DataFrame, then append it to the list
            for file_path in file_paths:
                df = pd.read_csv(file_path, header=None)
                datasets.append(df)
            print(datasets)
            print('\n')
            print('success 2')
            sleep(5)


            # pass

            # datasets_array = [df.values for df in datasets]
            # print(datasets_array)
            # sleep(2)


            # with open(new_info, 'r') as info:
            #     info_reader = csv.reader(info)
            #     info_data = list(info_reader)
                
            #     try:
            #         with open(entries, 'r') as entrie:

            #         info_data_array = np.array(info_data)
            #         # print('here')
            #         print(info_data_array)
            #         sleep(2)
            #     except:
            #         pass
            # Testing below:


            # result_matrix = predict_output(new_info_df, entries_df)
            # print("Input Matrix 1: ")
            # print(new_info_df)
            # print("Input Matrix 2: ")
            # printt(entries_df)
            # print('Predicted Output: ')
            # print(result_matrix)


            # csv_file_paths = [entries, new_info, payouts]
            # data_list = [entries_df.to_string(index=False), new_info_df.to_string(index=False), payouts_df.to_string(index=False)]

            # if len(entries_df) == 14:
            #     print('data_list is equal to 14 not 16')
            #     entries.write('0, 0, 0, 0, 0, 0')
            #     print(new_info)
            #     print(entries)
                # entries_df.append('0, 0, 0, 0, 0, 0')
                # entries_df.append('0, 0, 0, 0, 0, 0')

            data_list = [new_info_df, entries_df, payouts_df]
            # print(type(data_list))
            # print(len(data_list))
            # data_list_df = pd.DataFrame(data_list)
            # data_list.to_csv(filename3, sep=',', mode='a', index=False, encoding='utf-8')

            # data_list.to_csv(filename3, sep=',', mode='a', index=False, encoding='utf-8')

            # append_to_csv(new_info_df, entries_df, payouts_df, filename3)

            
            # print(data_list)
            # print(len(data_list[0]), len(data_list[1]), len(data_list[2]))

            # print(df.to_string(index=False))
            # sleep(2)



            # print(new_info_df)
            # new_info_df.to_csv(filename, sep=',', mode='a', index=False, encoding='utf-8')
            # #print(' ')
            # print(entries_df)
            # entries_df.to_csv(filename1, sep=',', mode='a', index=False, encoding='utf-8')
            # #print(' ')
            # print(payouts_df)
            # payouts_df.to_csv(filename2, sep=',', mode='a', index=False, encoding='utf-8')
            # print(' ')
            pass



# Specify the folder path you want to process
# folder_path = "/path/to/your/folder"

folder_path = "C:\\Users\\Tyler\\projects\\cybertooth-mod\\data\\aqueduct"
folder_path_test = "C:\\Users\\Tyler\\projects\\cybertooth-mod\\data\\aqueduct1"
folder_path_test1 = "C:\\Users\\Tyler\\projects\\cybertooth-mod\\data\\aqueduct-test"

# Call the function to process files in the folder
# process_files(folder_path)

process_files(folder_path_test1)


