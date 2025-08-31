# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Topic: Array, Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
class TwoSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def find_indices(self):
        num_to_index = {}
        for i, num in enumerate(self.nums):
            complement = self.target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

        return []

    
# Example usage:
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    two_sum = TwoSum(nums, target)
    result = two_sum.find_indices()
    print(f"Indices of the two numbers that add up to {target}: {result}")