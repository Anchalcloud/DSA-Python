# LeetCode 557 — Reverse Words in a String III

'''**Approach: String Manipulation + Two Pointers**

- Split the input sentence into individual words using `split()`.
- Traverse each word separately.
- Convert each word into a list because Python strings are immutable.
- Initialize two pointers:
  - `left = 0`
  - `right = len(word) - 1`
- Swap characters at both pointers until they meet.
- Convert the reversed character list back into a string using `"".join()`.
- Store each reversed word in a result list.
- Join all reversed words using a space separator.

**Time Complexity:** O(n), where n is the total number of characters.

**Space Complexity:** O(n) for the words and result storage.

**Key Learning:**
- Python strings are immutable, so convert them into lists for in-place character swapping.
- Two pointers can reverse characters efficiently.
- `split()` separates words, while `join()` combines characters and words.

**Pattern:** String Manipulation + Two Pointers'''

#SOLUTION
class Solution:
    def reverseWords(self, s: str) -> str:
        result=[]
        s1 = s.split()
        for char in s1:
            word= list(char)
            left=0
            right=len(word)-1
            while left < right:
                word[left] , word[right] = word[right] , word[left] 
                left+=1
                right-=1

            reversed_word = "".join(word)
            result.append( reversed_word )

        return " ".join(result)

        