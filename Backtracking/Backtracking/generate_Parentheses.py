
"""
LeetCode 22: Generate Parentheses

Approach: Backtracking (DFS)

- Generate valid parentheses combinations using recursion.
- Add an opening bracket if open_count < n.
- Add a closing bracket if close_count < open_count.
- Track opening and closing brackets separately.
- Add the completed combination when both counts reach n.
- Constraints ensure that invalid combinations are never generated.

Time Complexity: O(4^N / sqrt(N)), where N is the number of pairs.
Space Complexity: O(N) auxiliary space, excluding output.

"""


#solution
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        result=[]
        self.getParanthesis( n, 0, 0,  "" , result)
        return result


    def getParanthesis(self, n, open_count , close_count ,  path , result):

        if  open_count == n and close_count == n:
            result.append(path)
            return

        if open_count < n:
        
            self.getParanthesis( n, open_count+1, close_count, path + '(' , result)

        if close_count < open_count:
            
            self.getParanthesis( n, open_count, close_count+1, path + ')' , result)


        