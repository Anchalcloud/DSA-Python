"""
Problem: Partition to K Equal Sum Subsets

Approach: Backtracking with Pruning

Divide the array into k subsets with equal sums.

Track selected elements using a boolean array and build
one subset at a time. Sort in descending order, skip
duplicate choices, and prune branches that exceed the
target sum.
"""


#Solution
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:

        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k

        nums.sort(reverse=True)
        used = [False] * len(nums)
        current_sum = 0
        count = 0

        return self.getValue(nums, target, used, current_sum, count, 0, k )

    def getValue(self, nums, target, used, current_sum, count, index, k ):

        if count == k - 1:
            return True

        previous = None

        for i in range(index, len(nums)):
            if used[i]:
                continue
                
            if nums[i] == previous:
                continue
            previous = nums[i]

            if not used[i]:

                if current_sum + nums[i] > target:
                    continue

                used[i] = True

                if current_sum + nums[i] == target:
                   result =  self.getValue(nums, target, used, 0, count+1, 0, k )
                else:
                    result = self.getValue(nums, target, used, current_sum + nums[i], count, i+1, k )

                if result:
                    return True
        
                used[i] = False

                if current_sum == 0:
                    return False

        return False