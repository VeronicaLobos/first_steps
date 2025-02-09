def twoSum(nums, target):
    """
    Finds two numbers in a list (nums) that add up to
    a target value (target).
    Returns a list containing the indices of the two numbers
    that add up to the target, or an empty list if the pair
    does not exist.
    """

    num_map = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index

    return []


# test

array = [2, 5, 5, 7, 11, 15]
target_number = 10

print(twoSum(array, target_number))