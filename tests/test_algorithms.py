import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from algorithms.closest_pair import visualize_closest_pair
from algorithms.int_multiplication import visualize_integer_multiplication

class AlgorithmsTestCase(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="1.0 2.0\n2.5 3.5\n4.0 5.0\n")
    @patch("matplotlib.pyplot.savefig")
    def test_visualize_closest_pair(self, mock_savefig, mock_file):
        """Test visualize_closest_pair function for valid input data."""
        
        file_path = "dummy_file.txt"
        
        # Call the closest pair function with the dummy file path
        steps, result = visualize_closest_pair(file_path)
        
        # Check that the expected steps are in the result
        self.assertIn('Sorted all points by x-coordinate', steps)
        self.assertIn('Comparing points (1.0, 2.0) and (2.5, 3.5)', steps)
        self.assertIn('The closest pair is', result)
        
        # Check that savefig was called to save a plot (even though we are mocking it)
        self.assertTrue(mock_savefig.called)
        
        # Check if the result matches the expected closest pair output
        self.assertEqual(result, "The closest pair is ((1.0, 2.0), (2.5, 3.5)) with a distance of 2.24")

    @patch("builtins.open", new_callable=mock_open, read_data="10 20\n30 40\n")
    @patch("matplotlib.pyplot.savefig")
    def test_visualize_integer_multiplication(self, mock_savefig, mock_file):
        """Test visualize_integer_multiplication function for valid input data."""
        
        file_path = "dummy_multiplication_file.txt"
        
        # Call the integer multiplication function with the dummy file path
        steps, result = visualize_integer_multiplication(file_path)
        
        # Check that the expected steps are in the result
        self.assertIn('Multiplying 10 and 20', steps)
        self.assertIn('Karatsuba result of 10 and 20', steps)
        
        # Check the final result of the multiplication
        self.assertEqual(result, "The product of 10 and 20 is 200")
        
        # Check if savefig was called (even though we mock the plot saving)
        self.assertTrue(mock_savefig.called)

    @patch("builtins.open", new_callable=mock_open, read_data="1.0 2.0\n")
    def test_invalid_input_format_for_closest_pair(self, mock_file):
        """Test visualize_closest_pair function for invalid input format."""
        
        file_path = "invalid_file.txt"
        
        # Simulate an invalid input (single point instead of a pair)
        mock_file.return_value = StringIO("1.0 2.0\n")
        
        with self.assertRaises(ValueError):
            visualize_closest_pair(file_path)

    @patch("builtins.open", new_callable=mock_open, read_data="10,20\n30,40\n")
    def test_invalid_input_format_for_integer_multiplication(self, mock_file):
        """Test visualize_integer_multiplication for invalid input format."""
        
        file_path = "invalid_multiplication_file.txt"
        
        # Simulate an invalid format with commas instead of spaces
        mock_file.return_value = StringIO("10,20\n30,40\n")
        
        # Check if the format gets cleaned and parsed properly
        steps, result = visualize_integer_multiplication(file_path)
        
        self.assertIn('Multiplying 10 and 20', steps)
        self.assertEqual(result, "The product of 10 and 20 is 200")

if __name__ == '__main__':
    unittest.main()
