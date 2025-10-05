import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test that a list with no positive numbers returns a streak of 0."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_simple_streak():
    """Test a simple case with one streak."""
    assert longest_positive_streak([1, 2, 3, 0, 4]) == 3

def test_multiple_streaks():
    """Test that the function returns the length of the longest streak."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 0, 1]) == 3

def test_streak_at_the_end():
    """Test a case where the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, 7]) == 4

def test_zeros_and_negatives():
    """Test that zeros and negative numbers correctly break the streak."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_positive():
    """Test a list where all numbers are positive."""
    assert longest_positive_streak([1, 1, 1, 5, 2]) == 5