import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_all_positive():
    """Test a simple case with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_with_negatives():
    """Test that negative numbers break the streak."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros():
    """Test that zeros break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4]) == 2

def test_multiple_streaks():
    """Test that the function returns the longest of multiple streaks."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, -2, 1, 2]) == 3

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -5, 0]) == 0

def test_streak_at_end():
    """Test a case where the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 0, 2, 3, 4, 5]) == 4

def test_single_element_list():
    """Test lists with a single element."""
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([-1]) == 0
    assert longest_positive_streak([0]) == 0