import unittest
import pandas as pd

from duplicate_remover import DuplicateRemover
from os import remove


class FaceRecognitionStoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.data_remover = DuplicateRemover("test_data.csv", ".")

    def test_existing_data_remover(self):
        self.assertIsNotNone(self.data_remover)

    def test_column_names(self):
        column_names_default = ["given_name", "surname", "date_of_birth", "sex"]

        self.assertListEqual(column_names_default, self.data_remover.data.columns.tolist())

    def test_existing_preprocess_method(self):
        self.data_remover.preprocess()

    def test_preprocess_method_work(self):
        self.data_remover.preprocess()
        self.assertEqual(23, self.data_remover.data.shape[0])

    def test_existing_find_unique_method(self):
        self.data_remover.preprocess()
        self.data_remover.find_unique()

    def test_find_unique_method_work(self):
        self.data_remover.preprocess()
        self.data_remover.find_unique()
        self.assertEqual(22, self.data_remover.unique_data.shape[0])

    def test_existing_removing_duplicate_method(self):
        self.data_remover.preprocess()
        self.data_remover.find_unique()
        self.data_remover.remove_duplicates()

    def test_removing_duplicate_method_work(self):
        self.data_remover.preprocess()
        self.data_remover.find_unique()
        self.data_remover.remove_duplicates()
        self.assertEqual(21, self.data_remover.data_without_duplicates.shape[0])

    def test_existing_process_method(self):
        self.data_remover.process()

    def test_process_method_work(self):
        self.data_remover.process()

        saved_data = pd.read_csv("relateddata.csv")

        self.assertEqual(21, saved_data.shape[0])
        remove("relateddata.csv")
