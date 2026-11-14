
"""
LeetCode 93: Restore IP Addresses

Approach:
- Use backtracking to generate all possible valid IP addresses.
- Extract segments containing 1 to 3 digits.
- Validate each segment to ensure its value is between 0 and 255.
- Reject segments with leading zeros, except "0" itself.
- Maintain exactly four valid segments to form an IP address.
- Use append, recursion, and pop to explore and backtrack.

Time Complexity: O(1) because each IP address has exactly 4 segments,
with at most 3 choices per segment.

Auxiliary Space Complexity: O(1), as recursion depth and path length
are bounded by 4, excluding the output.
"""


#Solution

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        
        result = []
        self.getAddress(s, 0, [], result)
        return result

    def getAddress(self, s, index, path, result):

        if index == len(s):
            if len(path) ==  4:
                result.append(".".join(path))

            return result

        for i  in range(index, min(index+3, len(s))):
        
            segment=s[index:i+1]

            if segment == "0" or (segment[0] != "0" and int(segment) <= 255):
                if len(path) < 4:
                    path.append(segment)
            
                    self.getAddress(s, i+1, path, result)

                    path.pop()

            




        