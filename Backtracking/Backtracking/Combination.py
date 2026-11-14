
"""
LeetCode 77: Combinations

Approach:
- Use backtracking to generate combinations of size k from numbers 1 to n.
- Start choosing numbers from the current starting index.
- Append a number, recursively explore with i + 1, and backtrack using pop().
- When the path length reaches k, add a copy to the result.

Time Complexity: O(k * C(n, k))
Space Complexity: O(k) auxiliary space, excluding output.
"""

#solution

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        self.getCombination(n, k, 1, [], result)
        return result

    def getCombination(self, n, k, start, path, result):

        if len(path) == k:
            result.append(path.copy())
            return

        for i  in range(start,n+1):

            path.append(i)
            
            self.getCombination( n, k, i+1, path, result)

            path.pop()


