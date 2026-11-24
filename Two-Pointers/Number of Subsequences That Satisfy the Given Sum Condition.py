'''LeetCode 1498 — Number of Subsequences That Satisfy the Given Sum Condition

Approach: Sorting + Two Pointers + Combinatorics

Sort the array.

Use two pointers: i at the beginning and j at the end.

Check whether nums[i] + nums[j] <= target.

If true, every subsequence formed by including the minimum element and choosing any combination of elements between i and j is valid.

Add 2^(j-i) to the count and move i forward.

Otherwise, decrease j to reduce the maximum element.

Return the answer modulo 10^9 + 7.

Time Complexity: O(n log n)

Space Complexity: O(n) for the sorted copy; excluding the sorted copy, the two-pointer scan uses O(1) auxiliary space.

Key Learning:

A subsequence does not need to be contiguous.

The condition depends only on the minimum and maximum elements.

Combinatorics helps count multiple valid subsequences without generating them individually.

Pattern: Sorting + Two Pointers + Combinatorics'''

#Solution

class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:

        nums1  = sorted(nums)
        i= 0
        j= len(nums1) - 1
        count=0
        while  j >= i:
            
            if nums1[i] + nums1[j] <= target:
                count += 2** (j-i)
                i+=1
            else:
                j-=1

        return count%(10**9+7)



        