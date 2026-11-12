"""
LeetCode 79: Word Search
Topic: Backtracking / DFS
Difficulty: Medium

Approach:
1. Traverse every cell in the board.
2. Start DFS when a cell matches the first character.
3. Check the current character against word[index].
4. Explore four directions: up, down, left, right.
5. Mark the current cell as visited temporarily.
6. Restore the original character after exploring.

Key Concept:
Choose -> Explore -> Undo (Backtracking)

Time Complexity: O(m * n * 4 * 3^(L-1)) as a loose upper bound
Space Complexity: O(L) auxiliary recursion stack
"""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        if not word:
            return True

        if not board or not board[0]:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.getWord(board, word, 0, i, j):
                        return True

        return False

    def getWord(self, board, word, index, row, col):

        m = len(board)
        n = len(board[0])

        if index == len(word):
            return True

        if row < 0 or row >= m or col < 0 or col >= n:
            return False

        if board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = "#"

        found = (
            self.getWord(board, word, index + 1, row + 1, col) or
            self.getWord(board, word, index + 1, row - 1, col) or
            self.getWord(board, word, index + 1, row, col + 1) or
            self.getWord(board, word, index + 1, row, col - 1)
        )

        board[row][col] = temp

        return found