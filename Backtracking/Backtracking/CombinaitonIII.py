
"""
LeetCode 216: Combination Sum III

Approach:
- Use backtracking to find combinations of k distinct numbers from 1 to 9.
- Maintain a starting index to avoid duplicate numbers.
- Track the running sum to avoid repeatedly calculating sum(path).
- Prune branches when the running sum exceeds the target.
- When k numbers are selected, add the combination if the target sum is reached.

Time Complexity: O(k * 2^9) upper bound.
Space Complexity: O(k) auxiliary space, excluding output.
"""

#solution

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        
        result=[]
        self.getValue( k, n, 1, [], result,0)
        return result

    def getValue(self, k, n, start, path, result,  total):

        if len(path ) == k:
            if total == n:
                result.append(path.copy())        
            return

        for i in range(start, 10):
            path.append(i)

            if total+ i > n:
                path.pop()
                break

            self.getValue( k, n, i+1, path, result, total+i)

            path.pop()

