### LeetCode #2200 — Find All K-Distant Indices in an Array

'''Approach:** Two Pointers

- First, collected all indices where `nums[i] == key`.
- Used one pointer to traverse all array indices and another pointer to track the relevant key positions.
- Skipped key positions that were smaller than `j - k`.
- Checked whether the current key position was within `j + k`.
- Added valid indices to the result.

**Time Complexity:** \(O(n)\)

**Space Complexity:** \(O(m)\), where `m` is the number of occurrences of `key`.

**Key Learning:** Used two pointers to efficiently identify valid index ranges without repeatedly checking every key position.

**Pattern:** Two Pointers'''

#solution
class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        
        result= []
        key_points=[]

        i=0
        while i < len(nums):
            if nums[i] == key:
                key_points.append(i)
            i+=1
        
        p=0
        j=0
        while j < len(nums):
            
            while p < len(key_points) and key_points[p] < j-k :
                p+=1

            if p < len(key_points) and key_points[p] <= j+k:
                result.append(j)
                
            j+=1

        return result




        

