from unittest import TestCase
import file_handling
from settings import folder_path_1  # provide your own dirs to run unittests


class TestFileHandling(TestCase):
    def test_with_some_folder(self):
        self.assertGreater(len(file_handling.filenames_with_path(folder_path_1)), 10)

    def test_limit_ending(self):
        self.assertGreater(len(file_handling.filenames_with_path(folder_path_1, limit_ending='py')), 10)


class TestFileHandlingReadExcel(TestCase):
    def test_read_a_table(self):
        self.fail('not implemented')
