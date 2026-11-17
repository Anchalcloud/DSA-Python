"""
Problem: Word Break

Approach: Dynamic Programming / Memoization

Check whether the given string can be segmented into
valid words from the provided dictionary.

Explore possible prefixes and determine whether the
remaining suffix can also be segmented.
"""

#Solution
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        word_set = set(wordDict)
        max_len = max(map(len, word_set))
        
    #Top Down   Dynamic Programming

        memo={}
        return self.getMatch( s, word_set, 0, memo, max_len)
        
    def getMatch(self, s, word_set, index, memo, max_len):

        if len(s) == index:
            return True

        if index in memo:
            return memo[index]

        for i in range(index, min(len(s), index + max_len)):
            word = s[index:i+1]
            
            if word in word_set:
                if self.getMatch(s, word_set, i+1,memo, max_len):
                    memo[index]  = True
                    return True

        memo[index] = False
        return False
