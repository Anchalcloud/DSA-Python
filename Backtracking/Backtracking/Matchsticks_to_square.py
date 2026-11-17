"""
Problem: Matchsticks to Square

Approach: Backtracking with Pruning

Determine whether all matchsticks can be divided into
four groups with equal sums to form a square.

Build one side at a time using backtracking. Track used
matchsticks with a boolean array and track the current
side sum and completed sides.

Sort matchsticks in descending order and prune branches
that exceed the target sum. Use symmetry pruning to avoid
exploring equivalent side combinations.
"""

#Solution
class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:

        total = sum(matchsticks)
        target = total // 4

        matchsticks.sort(reverse=True)
        used = [False]*len(matchsticks)
        current_sum = 0
        count=0

        if total % 4 != 0:
            return False

        if len(matchsticks) < 4:
            return False

        if max(matchsticks) > target:
            return False

        return self.getMatchsticks(matchsticks, current_sum, count, used, target, 0)

    def getMatchsticks(self, matchsticks, current_sum, count, used, target, index):

        if count == 4:
            return True

        for i in range(index, len(matchsticks)):

            if not used[i]:

                if current_sum + matchsticks[i]> target:
                    continue
                    
                used[i] = True

                if current_sum + matchsticks[i] == target:
                    result  = self.getMatchsticks(matchsticks,0, count+1, used,target, 0 )
                else:
                    result = self.getMatchsticks(matchsticks,current_sum + matchsticks[i] , count, used, target, i + 1 )

                if result:
                    return True

                used[i] = False

                if  current_sum == 0:
                    return False  

        
        