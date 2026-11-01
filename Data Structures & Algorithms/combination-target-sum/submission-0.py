class Solution:
    def util(self, ind, curr_sum, combination, target, results, n, nums):
        if curr_sum == target:
            results.append(combination)
            return

        if ind == n or curr_sum > target:
            return

        # picking the element?
        self.util(ind, curr_sum + nums[ind], combination + [nums[ind]], target, results, n, nums)

        self.util(ind + 1, curr_sum, combination, target, results, n, nums)

        return

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        2, 5, 6, 9

        I can use a number as many time as I need right, this means we
        necessarily need to increase the index

        if curr_sum == target:
            result.append(combination)
            return 
        if ind >= n:
            return 

        // pick 2
        use the same ind

        // not  pick 2
        increase ind
        """

        n = len(nums)
        combination = []
        curr_sum = 0
        start = 0
        results = []

        self.util(start, curr_sum, combination, target, results, n, nums)

        return results
