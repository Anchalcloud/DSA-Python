'''# LeetCode 1679 — Max Number of K-Sum Pairs

**Approach: Sorting + Two Pointers**

- Sort the array in ascending order.
- Initialize two pointers: `i` at the beginning and `j` at the end.
- Calculate the sum of the elements at both pointers.
- If the sum equals `k`:
  - Increment the pair count.
  - Move both pointers inward.
- If the sum is less than `k`, move `i` forward to increase the sum.
- If the sum is greater than `k`, move `j` backward to decrease the sum.
- Continue until the pointers cross.
- Return the total number of operations (pairs).

**Time Complexity:** O(n log n)

**Space Complexity:** O(n) for the sorted copy; O(1) auxiliary space for the two-pointer scan.

**Key Learning:**
- Sorting makes it easier to find pairs with a target sum.
- Two pointers help avoid checking every possible pair.
- Each element can be used in at most one pair.

**Pattern:** Sorting + Two Pointers + Greedy'''

#solution
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums1= sorted(nums)        
        count=0
        i=0
        j=len(nums1)-1
        while i < j:
            if nums1[i] + nums1[j] == k:
                count+=1
                i+=1
                j-=1
            elif nums1[i]  + nums1[j] > k:
                j-=1
            else:
                i+=1

        return count