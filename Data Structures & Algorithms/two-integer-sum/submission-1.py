class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target-nums[i]], i]

            if nums[i] in hash:
                continue
            else:
                hash[nums[i]] = i

        return [-1, -1]