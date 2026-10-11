class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()

        for r, val in enumerate(nums):
            # Removing older candidates:
            while dq and dq[0][1] < r - k + 1:
                dq.popleft()
            
            # Removing weaker candidates:
            while dq and dq[-1][0] < val:
                dq.pop()
            
            dq.append([val, r])

            if r >= k - 1:
                result.append(dq[0][0])

        return result