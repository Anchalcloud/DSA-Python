"""
LeetCode 1863: Sum of All Subset XOR Totals

Topic: Backtracking / Recursion
Difficulty: Easy

Approach:
1. For each element, explore two choices:
   - Include the current element.
   - Skip the current element.
2. Use backtracking to explore all possible subsets.
3. At the base case, calculate the XOR of the current subset.
4. Return the sum of XOR totals from both recursive branches.

Backtracking Pattern:
Choose -> Explore -> Undo

Complexity Analysis:
Time Complexity: O(N * 2^N)
Auxiliary Space Complexity: O(N) for recursion and the current subset.
"""

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        return self.getSubset(nums, 0, [])

    def getSubset(self, nums, index, combine):

        if index == len(nums):
            x = 0
            for num in combine:
                x ^= num
            return x

        # Include current element
        combine.append(nums[index])
        include = self.getSubset(nums, index + 1, combine)
        combine.pop()

        # Skip current element
        exclude = self.getSubset(nums, index + 1, combine)

        return include + exclude