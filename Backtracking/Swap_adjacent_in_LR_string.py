LeetCode 777 – Swap Adjacent in LR String

Difficulty: Medium
Topics: Two Pointers, String

Approach

Used two pointers to traverse start and result.

Skipped all X characters in both strings.

Compared the remaining characters to ensure their order was identical.

Checked movement restrictions:

L can only move left (end_index <= start_index).

R can only move right (end_index >= start_index).

Skipped remaining X characters and verified that both strings were fully processed.

Complexity

Time Complexity: O(n)
Space Complexity: O(1)

#Solution
class Solution(object):
    def canTransform(self, start, result):
        
        i = 0
        j = 0

        while i < len(start) and j < len(result):

            while i < len(start) and  start[i] == 'X':
                i += 1

            while j < len(result) and result[j] == 'X':
                j += 1
            
            if i == len(start) or j == len(result):
                return i == len(start) and j == len(result)

            if start[i] != result[j]:
                return False
            
            if start[i] == 'L' and j > i :
                return False
        
            if  start[i] == 'R'  and i > j:
                return False

            i+=1
            j+=1
         
        while i < len(start) and start[i] == 'X':
            i+= 1

        while j < len(result) and result[j] == 'X':
            j += 1

        return i == len(start) and j == len(result)