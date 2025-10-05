def longest_positive_streak(nums: list[int]) -> int:
    """
    Calculates the length of the longest run of consecutive values strictly greater than 0.

    - An empty list returns 0.
    - Non-positive numbers break the streak (0 or negatives reset the count).
    - The function must be deterministic and pure: no randomness, prints, or global state.
    """
    max_streak = 0
    current_streak = 0
    for num in nums:
        if num > 0:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 0
    max_streak = max(max_streak, current_streak)
    return max_streak