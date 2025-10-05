from typing import List

def longest_positive_streak(nums: List[int]) -> int:
    """
    Calculates the length of the longest consecutive run of strictly positive integers.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest streak of positive numbers. Returns 0 for an empty list.
    """
    if not nums:
        return 0

    max_streak = 0
    current_streak = 0

    for num in nums:
        if num > 0:
            current_streak += 1
        else:
            if current_streak > max_streak:
                max_streak = current_streak
            current_streak = 0

    # Final check in case the longest streak is at the end of the list
    if current_streak > max_streak:
        max_streak = current_streak

    return max_streak