class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prev = [0] * n
        next = [0] * n

        for i in range(n):
            if i == 0:
                prev[i] = 1
                continue
                
            prev[i] = nums[i - 1]*prev[i - 1]

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                next[i] = 1
                continue
                
            next[i] = nums[i + 1]*next[i + 1]
            
        result = []
        for i in range(n):
            result.append(prev[i]*next[i])

        return result