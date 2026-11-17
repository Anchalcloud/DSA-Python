"""
Problem: Maximum Length of a Concatenated String with Unique Characters

Approach: Backtracking

Explore two choices for each string: include it if all its
characters are unique and do not overlap with the selected
characters, or skip it.

Use a set to track selected characters and backtrack by
removing the added characters after exploring the include
branch. Return the maximum length across both branches.
"""
#solution
class Solution:
    def maxLength(self, arr: list[str]) -> int:

        selected= set()
        return self.getString(arr, selected, 0)

    def getString(self, arr, selected,  index):

        if len(arr) == index:
            return len(selected)

        include=0

        if len(set(arr[index])) == len(arr[index]) and all(char not in selected for char in arr[index]):
            for char in arr[index]:
                selected.add(char)
                
            include = self.getString(arr, selected, index+1)

            for char in arr[index]:
                selected.remove(char)

        skip = self.getString(arr, selected, index+1)

        return max(include, skip)
       
    






        
        
        
