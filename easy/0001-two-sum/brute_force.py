# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Topic: Array
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class TwoSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def find_indices(self):
        n = len(self.nums)
        for i in range(n):
            for j in range(i+1, n):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i, j]
                
        return []


# Example usage:
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    two_sum = TwoSum(nums, target)
    result = two_sum.find_indices()
    print(f"Indices of the two numbers that add up to {target}: {result}")
