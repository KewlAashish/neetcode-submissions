class Solution:
    def util(self, ind, combination, curr_sum, target, nums, results):
        if curr_sum > target:
            return

        if curr_sum == target:
            results.append(combination)
            return

        if ind >= len(nums):
            return

        # pick
        self.util(ind + 1, combination + [nums[ind]], curr_sum + nums[ind], target, nums, results)

        # not pick
        next_ind = ind + 1

        while next_ind < len(nums) and nums[next_ind] == nums[ind]:
            next_ind += 1

        self.util(next_ind, combination, curr_sum, target, nums, results)

        return


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        pick an element, then increase ind
        not pick an element still increase ind
        There can be duplicate elements, so we have to be comfortable with 
        the unique

        The problem lies here: [2, 2, 4] and target = 6
        I may get a duplicate: [2, 4] where 2 is ind 0
        and [2, 4] where 2 is ind 1. So we have a problem here

        Another gaps in [2, 4] and [4, 2] being stored which are duplication combinations.

        if not picking and prev is same, then I have to be extra careful in skipping it?
        Like prev_ind = 2 and curr_ind = 2 then we should only pick if in the combination we picked 2 earlier else go with no picking. But looks like
        an over complication.

        Why not make sure, results have a unique set likee thing?
        """
        candidates.sort()
        results = []

        self.util(0, [], 0, target, candidates, results)

        return results