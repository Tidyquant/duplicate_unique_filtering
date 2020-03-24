import numpy as np
import pandas as pd

from Levenshtein import distance as levenshtein_distance
from time import time
from tqdm import tqdm


class DuplicateRemover:
    """
    Class for removing duplicates
    """

    def __init__(self, data_path, folder_to_save, threshold=2):
        """
        Init function for duplicate remover.
        :param data_path: path to the file with data.
        :param folder_to_save: path to the folder where the processed file has to be saved.
        :param threshold: maximum value for returned Levenshtein distance between two samples in data
        """
        # Read data from source
        self.data = pd.read_csv(data_path)
        # Replace missed values by empty string
        self.data = self.data.fillna("")
        self.duplicated_data = None
        self.unique_data = None
        self.data_without_duplicates = None
        self.threshold = threshold
        self.folder_to_save = folder_to_save

    def process(self):
        """
        Function for process data and save new data without duplicates.
        1. Preprocess source data.
        2. Find unique values in source data.
        3. Drop duplicate names from source data.
        4. Drop extra columns.
        5. Save data without duplicates in names.
        """
        self.preprocess()
        self.find_unique()
        self.remove_duplicates()
        self.data_without_duplicates = self.data_without_duplicates.drop(columns=['full_name', 'find_unique'])
        self.duplicated_data = self.duplicated_data.drop(columns=['full_name', 'find_unique'])
        self.data_without_duplicates.to_csv(f"{self.folder_to_save}/uniquedata.csv", index=False)
        self.duplicated_data.to_csv(f"{self.folder_to_save}/duplicateddata.csv", index=False)

    def preprocess(self):
        """
        Function for preprocess data.
        Merge given_name and surname to validate names.
        Merge [date_of_birth, sex, full_Name] columns to find right unique_values.
        """
        self.data['full_name'] = self.data["given_name"] + " " + self.data["surname"]
        self.data['find_unique'] = self.data['date_of_birth'] + " " + self.data['sex'] + " " + self.data['full_name']

    def find_unique(self):
        """
        Function for finding unique values in data.
        Save dataframe with unique records from source data in unique_data field.
        """
        self.data["duplicated"] = self.data.duplicated(subset="find_unique").astype(int)
        self.duplicated_data = self.data[self.data["duplicated"] == 1]
        self.unique_data = self.data[self.data["duplicated"] == 0]

    def remove_duplicates(self):
        """
        Function for removing duplicate names in data.
        Save dataframe with different people from source data in data_without_duplicates field.
        """
        dupl_indexes = []
        rows_number = self.unique_data.shape[0]
        for i in tqdm(range(rows_number - 1)):
            distances = np.array(
                [levenshtein_distance(self.unique_data["full_name"].values[i],
                                      self.unique_data["full_name"].values[j]) for j in
                 range(i + 1, rows_number)])
            matching_indexes = np.where(distances <= self.threshold)[0]
            matching_indexes = matching_indexes + i + 1

            d_b1 = self.unique_data['date_of_birth'].iloc[i]
            dupl_indexes += [self.unique_data.index[match] for match in matching_indexes if
                             self.unique_data['date_of_birth'].iloc[match] == d_b1]
        self.data_without_duplicates = self.unique_data.copy()
        self.duplicated_data = self.duplicated_data.append(self.unique_data.loc[dupl_indexes])
        self.data_without_duplicates = self.data_without_duplicates.drop(dupl_indexes)
