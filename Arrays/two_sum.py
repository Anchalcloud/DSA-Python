# Problem: Two Sum
# LeetCode: https://leetcode.com/problems/two-sum/
# Topic: Arrays
# Approach: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

# Accepted Solution

class Solution:
  def twoSum( self, nums, target):
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[i] + nums[j] == target:
                    return [i , j] 
                j+=1
            i+=1