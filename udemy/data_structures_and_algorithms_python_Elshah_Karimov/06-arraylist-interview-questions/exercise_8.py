# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def contains_duplicate(nums):
    for i in range(len(nums)):
        if nums.count(i) > 1:
            return True
    return False