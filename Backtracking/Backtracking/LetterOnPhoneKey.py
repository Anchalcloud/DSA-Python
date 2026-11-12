"""
LeetCode 17: Letter Combinations of a Phone Number

Approach: Backtracking (DFS)

- Map each digit to its corresponding letters.
- Explore every possible letter combination recursively.
- Add a combination when all digits have been processed.
- Backtrack to explore other possible combinations.

Time Complexity: O(4^N * N)
Space Complexity: O(N)
"""


#solution

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        ans =[]
        values=[]
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        self.getValue(digits, 0, phone, ans, values)
        return ans

    def getValue(self, digits, index, phone, ans, values):

        if len(digits) == index:
            ans.append("".join(values))
            return 

        if not digits:
            return []

        letters = phone[digits[index]]
        for i in range(len(letters)):

            values.append(letters[i])

            self.getValue(digits, index+1, phone,ans, values)

            values.pop()