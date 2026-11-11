
# Problem: 3Sum
# LeetCode: https://leetcode.com/problems/3sum/
# Topic: Arrays, Two Pointers
# Approach: Sorting + Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1) auxiliary space (excluding sorting)

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        i = 0

        while i < len(nums) - 2:
            left = i + 1
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    result.append(triplet)

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total > 0:
                    right -= 1
                else:
                    left += 1

            i += 1

        return result
