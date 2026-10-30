class Solution:
    def util(self, results, ind, nums, set_till_now):
        if ind == len(nums):
            results.append(set_till_now)
            return
        
        # pick
        self.util(results, ind + 1, nums, set_till_now + [nums[ind]])
        self.util(results, ind + 1, nums, set_till_now)

        return


    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given we have to create all possible subset's this problem screams
        recursion. Now we can come up with a recursive solution first then
        see if something with DP can be done

        What is a subset?
        [1, 2, 3] -> [], [1], [1, 2], [1, 3], [1, 2, 3], [2], [2, 3], [3]

        Kinda feels like we have to either pick an index and or not pick it?
        If picked?
            call next ind and if not insert in the final set
            but do add this picked element in the subset we are maintaining
        if not picked?
            call next ind anyways and if not insert in the final set
        
        []
       [1][]
      [1,2][1][] 
        """
        result = []
        self.util(result, 0, nums, [])

        return result