### LeetCode #475 — Heaters

**Approach:** Sorting + Two Pointers

- Sorted both `houses` and `heaters` arrays.
- Used two pointers to track each house and its nearest heater.
- Moved the heater pointer forward whenever the next heater was closer or equally close.
- Calculated the minimum distance for each house and maintained the maximum distance as the required radius.

**Time Complexity:** \(O(n\log n + m\log m)\)

**Space Complexity:** \(O(n+m)\) for sorted copies of the arrays.

**Key Learning:** Handling duplicate heater positions and equal-distance comparisons correctly. Used `>=` instead of `>` to avoid getting stuck before a closer heater when duplicate positions exist.

**Pattern:** Two Pointers + Greedy

#solution
class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:

        house = sorted(houses)
        heater = sorted(heaters)

        i=0
        j=0
        max_radius=0
        while i < len(house):  

            while j+1 < len(heater) and abs(house[i]- heater[j]) >= abs(house[i] - heater[j+1]):
                j+=1

            distance = abs(house[i] - heater[j])
            max_radius = max(max_radius, distance)
            i+=1
        return max_radius
    