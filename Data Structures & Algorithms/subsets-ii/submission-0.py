class Solution:

    def util(self, ind, curr, nums, results):
        if ind == len(nums):
            results.append(curr.copy())
            return

        # pick
        curr.append(nums[ind])
        self.util(ind + 1, curr, nums, results)
        curr.pop()

        # not pick
        next_ind = ind + 1

        while next_ind < len(nums) and nums[next_ind] == nums[ind]:
            next_ind += 1

        self.util(next_ind, curr, nums, results)
        

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Don't see any reason why this cannot be a pick / not pick kinda problem?
        """
        nums.sort()
        results = []
        
        self.util(0, [], nums, results)

        return results