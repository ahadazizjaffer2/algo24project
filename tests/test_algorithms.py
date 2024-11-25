import pytest
from algorithms.closest_pair import visualize_closest_pair
from algorithms.int_multiplication import visualize_integer_multiplication

def test_closest_pair_algorithm():
    """Test the closest pair algorithm"""
    steps, result = visualize_closest_pair('test_cp.txt')
    assert 'Closest pair' in result
    assert len(steps) > 0  # Ensure steps were generated

def test_integer_multiplication_algorithm():
    """Test the integer multiplication algorithm"""
    steps, result = visualize_integer_multiplication('test_im.txt')
    assert 'Karatsuba result' in result
    assert len(steps) > 0  # Ensure steps were generated
