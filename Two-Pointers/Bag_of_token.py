'''LeetCode 948 — Bag of Tokens

Approach: Sorting + Two Pointers + Greedy

Sort the tokens in ascending order.

Use two pointers: i at the smallest token and j at the largest token.

If the smallest token can be purchased with the available power, play it face-up:

Decrease power by its value.

Increase score by 1.

Move i forward.

Otherwise, if the score is at least 1, play the largest remaining token face-down:

Increase power by its value.

Decrease score by 1.

Move j backward.

If the smallest token cannot be purchased and the score is 0, stop because no valid move is possible.

Maintain max_score because the current score can decrease after a face-down move.

Return the maximum score achieved.

Time Complexity: O(n log n)

Space Complexity: O(n) for the sorted copy; excluding the sorted copy, the two-pointer scan uses O(1) auxiliary space.

Key Learning:

Greedy decisions help maximize the score.

Use the smallest token to gain score efficiently.

Use the largest token to regain power when necessary.

Track the maximum score rather than only the final score.

Pattern: Sorting + Two Pointers + Greedy'''

#Solution
class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        token = sorted(tokens)
        i=0
        j= len(token) -1
        score=0
        max_score = 0
        while i <= j:
            if  score == 0 and power < token[i]:
                break
            if token[i] <= power:
                power = power - token[i]
                score+=1
                max_score = max(score, max_score)
                i+=1
            elif score >= 1 and  token[i] > power:
                power = power+ token[j] 
                score-=1
                j-=1

        return max_score