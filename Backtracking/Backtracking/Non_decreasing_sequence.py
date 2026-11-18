"""
Problem: Non-decreasing Subsequences

Approach: Backtracking with Duplicate Handling

Generate all unique non-decreasing subsequences of length
at least two.

Use recursion to explore valid elements while maintaining
the original order. Track the current subsequence using a
path and backtrack after each choice.

Use a set at each recursion level to avoid generating
duplicate subsequences.
"""

#Solution
class Solution(object):
    def findSubsequences(self, nums):

        result=[]
        self.newSequence( nums, 0 ,  [], result  )
        return result

    def newSequence(self, nums,  index,  path,result):
        
        if len(path) >= 2:
            result.append(path.copy())
        
        if index == len(nums):
            return
    
        used=set()

        for i in range(index, len(nums)):

            if nums[i] in  used:
                continue

            used.add(nums[i])

            if len(path) == 0 :
                path.append(nums[i])
                self.newSequence( nums, i+1 ,  path ,result)
                path.pop()
            else:
                if  nums[i] >= path[-1]:
                    path.append(nums[i])

                    self.newSequence( nums, i+1 ,  path ,result)

                    path.pop()
                    
                
        



                       
        