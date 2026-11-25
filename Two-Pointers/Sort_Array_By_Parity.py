'''LeetCode 905 — Sort Array By Parity

Approach: Two Pointers

Initialize two pointers: i at the beginning and j at the end.

If the left element is even, move i forward.

If the right element is odd, move j backward.

If the left element is odd and the right element is even, swap them.

Continue until the pointers cross.

Time Complexity: O(n)

Space Complexity: O(1)

Key Learning:

Two pointers can partition an array based on a condition.

Swapping misplaced elements avoids creating another array.

Even numbers can be placed before odd numbers in-place.

Pattern: Two Pointers + In-place Array Partitioning'''

#solution
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left=0
        right = len(nums)-1
        while  left < right:
            if nums[left] %2 != 0 and nums[right]%2 ==0 :
                nums[left] , nums[right]  = nums[right], nums[left]
                left+=1
                right-=1
            elif nums[right] % 2 != 0:
                right-=1
            else:
                left+=1

        return nums