class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        end = -1
        for i in piles:
            end = max(end, i)

        def util(rate):
            time = 0
            for i in piles:
                if i % rate == 0:
                    time += i // rate
                else:
                    time += int(i // rate) + 1
            
            return True if time <= h else False

        start = 1
        ans = float("inf")
        while start <= end:
            mid = (start + end) // 2

            if util(mid):
                ans = min(ans, mid)
                end = mid - 1
            else:
                start = mid + 1

        return ans