import unittest
import pandas as pd

from duplicate_finder.duplicate_remover import DuplicateRemover
from os import remove


class DuplicateRemoverTest(unittest.TestCase):
    def setUp(self) -> None:
        self.duplicate_remover = DuplicateRemover("test_data.csv", ".")

    def test_existing_data_remover(self):
        """
        Test if duplicate remover class exists.
        """
        self.assertIsNotNone(self.duplicate_remover)

    def test_column_names(self):
        """
        Test if column names have needed values.
        """
        column_names_default = ["given_name", "surname", "date_of_birth", "sex"]

        self.assertListEqual(column_names_default, self.duplicate_remover.data.columns.tolist())

    def test_existing_preprocess_method(self):
        """
        Test if preprocess method of duplicate remover class exists.
        """
        self.duplicate_remover.preprocess()

    def test_preprocess_method_work(self):
        """
        Test if preprocess method work correctly.
        """
        self.duplicate_remover.preprocess()
        self.assertEqual(23, self.duplicate_remover.data.shape[0])

    def test_existing_find_unique_method(self):
        """
        Test if find_unique method of duplicate remover class exists.
        """
        self.duplicate_remover.preprocess()
        self.duplicate_remover.find_unique()

    def test_find_unique_method_work(self):
        """
        Test if find_unique method work correctly.
        """
        self.duplicate_remover.preprocess()
        self.duplicate_remover.find_unique()
        self.assertEqual(22, self.duplicate_remover.unique_data.shape[0])

    def test_existing_removing_duplicate_method(self):
        """
        Test if removing_duplicate method of duplicate remover class exists.
        """
        self.duplicate_remover.preprocess()
        self.duplicate_remover.find_unique()
        self.duplicate_remover.remove_duplicates()

    def test_removing_duplicate_method_work(self):
        """
        Test if removing_duplicate method work correctly.
        """
        self.duplicate_remover.preprocess()
        self.duplicate_remover.find_unique()
        self.duplicate_remover.remove_duplicates()
        self.assertEqual(21, self.duplicate_remover.data_without_duplicates.shape[0])

    def test_existing_process_method(self):
        """
        Test if process method of duplicate remover class exists.
        """
        self.duplicate_remover.process()

    def test_process_method_work(self):
        """
        Test if process method work correctly.
        """
        self.duplicate_remover.process()

        saved_data = pd.read_csv("relateddata.csv")

        self.assertEqual(21, saved_data.shape[0])
        remove("relateddata.csv")
