
"""
Problem: Word Break II

Approach: Backtracking with Memoization

Generate all possible sentences by splitting the string
into valid dictionary words.

Use recursion to explore valid prefixes, maintain the
current sentence using a path, and backtrack after each
choice. Memoization avoids recomputing overlapping suffixes.
"""

#Solution
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:

    #basic recursion and backtracking
        result= []
        self.getValue( s, wordDict, 0, [], result)
        return result

    def  getValue(self, s, wordDict, index, path, result):
        if index == len(s):
            result.append(" ".join(path))
            return 

        for i in range(index, len(s)):

            word= s[index:i+1]

            if word in wordDict:
                path.append(word)

                self.getValue( s, wordDict, i+1, path, result)

                path.pop()


    # dynamic programming
        memo = {}
        word_set = set(wordDict)
        return self.getValue(s, word_set, 0, memo)

    def getValue(self, s, word_set, index, memo):

        if index == len(s):
            return [""]

        if index in memo:
            return memo[index]

        sentence =[]

        for i in range(index, len(s)):

            word= s[index:i+1]
            if word in word_set:

                suffixes = self. getValue( s, word_set, i+1, memo)

                for suffix in suffixes:
                    sentence.append(f"{word} {suffix}".strip())

        memo[index] = sentence
        return sentence
            

            





        
    