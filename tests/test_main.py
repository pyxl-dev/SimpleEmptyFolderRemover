import unittest
import main
from pathlib import Path


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        print("setUp")
        self.test_folder = Path('./test_folder')
        # Create test folder
        self.test_folder.mkdir(parents=True, exist_ok=True)

    def tearDown(self) -> None:
        print("tearDown")
        # Remove test folder
        self.test_folder.rmdir()

    def test_remove_empty_folders(self):
        print("test_remove_empty_folders")
        # Create multiple folders
        for i in range(3):
            self.test_folder.joinpath(str(i)).mkdir(parents=True, exist_ok=True)
        main.remove_empty_folders(self.test_folder)
