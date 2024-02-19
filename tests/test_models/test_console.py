import unittest
from unittest.mock import patch
from console import HBNBCommand

class TestCreateCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_valid_params(self, mock_stdout):
        # Redirect stdout to capture printed output

        # Create an instance of the command interpreter
        console = HBNBCommand()

        # Mock user input for testing
        with patch('builtins.input', return_value='create BaseModel name="Test" value=42'):
            console.onecmd('create BaseModel name="Test" value=42')

        # Assert that the instance is created and ID is printed
        self.assertIn("Test", mock_stdout.getvalue())
        self.assertIn("42", mock_stdout.getvalue())
        # Add more assertions based on your specific implementation

    # Add more test cases for different scenarios

if __name__ == '__main__':
    unittest.main()

