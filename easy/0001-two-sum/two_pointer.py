# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Topic: Array, Two Pointers
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for storing the sorted array with original indices
class TwoSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def find_indices(self):
        # Create a list of tuples (num, index) and sort it
        sorted_nums = sorted((num, i) for i, num in enumerate(self.nums))
        left, right = 0, len(sorted_nums) - 1

        while left < right:
            current_sum = sorted_nums[left][0] + sorted_nums[right][0]
            if current_sum == self.target:
                return [sorted_nums[left][1], sorted_nums[right][1]]
            elif current_sum < self.target:
                left += 1
            else:
                right -= 1

        return []


# Example usage:
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    two_sum = TwoSum(nums, target)
    result = two_sum.find_indices()
    print(f"Indices of the two numbers that add up to {target}: {result}")
