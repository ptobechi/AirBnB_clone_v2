import unittest
from unittest.mock import patch
from models import storage
from os import environ


class TestStorageInstantiation(unittest.TestCase):
    """
    Test case to ensure correct instantiation of storage based on HBNB_TYPE_STORAGE
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class-level configurations before running tests
        """
        # Save the original value of HBNB_TYPE_STORAGE
        cls.original_storage_type = environ.get("HBNB_TYPE_STORAGE")

    @classmethod
    def tearDownClass(cls):
        """
        Clean up class-level configurations after running tests
        """
        # Restore the original value of HBNB_TYPE_STORAGE
        environ["HBNB_TYPE_STORAGE"] = cls.original_storage_type

    def setUp(self):
        """
        Set up configurations before each test
        """
        # Reset storage instance before each test
        storage.__class__.reset()

    @patch.dict("os.environ", {"HBNB_TYPE_STORAGE": "db"})
    def test_storage_instantiation_db(self):
        """
        Test storage instantiation when HBNB_TYPE_STORAGE is set to 'db'
        """
        # Import storage to trigger the instantiation based on the patched environment variable
        from models import storage as db_storage

        # Assert that the correct storage type is instantiated
        self.assertEqual(db_storage.__class__.__name__, "DBStorage")

    @patch.dict("os.environ", {"HBNB_TYPE_STORAGE": "file"})
    def test_storage_instantiation_file(self):
        """
        Test storage instantiation when HBNB_TYPE_STORAGE is set to 'file'
        """
        # Import storage to trigger the instantiation based on the patched environment variable
        from models import storage as file_storage

        # Assert that the correct storage type is instantiated
        self.assertEqual(file_storage.__class__.__name__, "FileStorage")

    def test_default_storage_instantiation(self):
        """
        Test storage instantiation with the default storage type
        """
        # Import storage to trigger the instantiation without the patched environment variable
        from models import storage as default_storage

        # Assert that the correct default storage type is instantiated
        self.assertEqual(default_storage.__class__.__name__, "FileStorage")


if __name__ == "__main__":
    unittest.main()
