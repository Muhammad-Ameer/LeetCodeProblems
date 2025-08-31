# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Topic: Array, Binary Search
# Time Complexity: O(n log n) due to sorting and binary search
# Space Complexity: O(n) for storing the sorted array with original indices
class TwoSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    @staticmethod
    def binary_search(arr, left, right, x):
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] == x:
                return mid
            elif arr[mid][0] < x:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def find_indices(self):
        # Create a list of tuples (num, index) and sort it
        sorted_nums = sorted((num, i) for i, num in enumerate(self.nums))

        for i in range(len(sorted_nums)):
            complement = self.target - sorted_nums[i][0]
            j = self.binary_search(sorted_nums, i + 1, len(sorted_nums) - 1, complement)
            if j != -1:
                return [sorted_nums[i][1], sorted_nums[j][1]]

        return []


# Example usage:
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    two_sum = TwoSum(nums, target)
    result = two_sum.find_indices()
    print(f"Indices of the two numbers that add up to {target}: {result}")
