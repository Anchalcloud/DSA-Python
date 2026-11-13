
"""
LeetCode 784: Letter Case Permutation

Approach: Backtracking (DFS)

- Process each character using recursion.
- If the character is a digit, keep it unchanged.
- If it is a letter, explore two choices:
  1. Convert it to lowercase.
  2. Convert it to uppercase.
- Add the completed string when all characters are processed.

Time Complexity: O(N * 2^L)
Space Complexity: O(N) auxiliary space.

N = Length of input string
L = Number of letters in the string
"""

#solution

class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:

        result = []
        self.getPermutation(s, 0, "", result)
        return result

    def getPermutation(self, s, index, path, result):

        if len(s) == index:
            result.append(path)
            return 

        if s[index].isdigit():
            path + s[index]
            self.getPermutation(s, index+1, path + s[index], result)
            return

        #include lower()
        self.getPermutation(s, index+1, path + s[index].lower(), result)

        #upper()
        self.getPermutation(s, index+1, path + s[index].upper(), result)







     
        