'''LeetCode 643 — Maximum Average Subarray I

Pattern: Fixed-Size Sliding Window

Approach

Calculate the sum of the first k elements to create the initial window.

Move the window one position at a time.

Subtract the outgoing element and add the incoming element to update the window sum.

Calculate the average for each window and maintain the maximum average.

Since every window has exactly k elements, maximizing the sum also maximizes the average.

Complexity

Time: O(n)

Space: O(1)

Key Learning

Instead of recalculating the sum for every subarray, reuse the previous window sum by removing one element and adding another.

Important: Initialize the maximum average with negative infinity to handle arrays containing only negative numbers.'''

#Solution
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        left=0
        right=0
        current_sum=0
        max_average = float('-inf')
        while left <= len(nums)-k:
            while right < k:
                current_sum +=nums[right]
                right+=1

            average = current_sum / k
            max_average = max(max_average, average)
            
            if right < len(nums):
                current_sum -=nums[left]
                current_sum += nums[right]
                left+=1
                right+=1
            else:
                break
        return max_average
    
