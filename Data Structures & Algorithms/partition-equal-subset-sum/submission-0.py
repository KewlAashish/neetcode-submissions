class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        1, 2, 3, 4

        Partition at index ind
        prev -> ind and ind + 1 -> end
        Is the sum equal? Then yes
        Else continue

        Now the efficiency part looks like it will come into picture because how will you check the sum in O(1)?

        There comes the prefix sum, like sum of elements till ind, excluding ind?
        prefix[ind] = sum (0 to ind - 1)

        prefix[ind + 1] and prefix [n - 1] + nums[n] - prefix[ind + 1] are equal?

        But I do feel why not instead of prefix I use, something like sum_till_ind
        including ind as well

        BUT Bro we are not looking for subarrays, but we are looking for subsets man

        We need to find the middle ground

        1, 2, 3, 4
        total sum = 10

        A subset with sum = 10 will solve the problem.

        pick/not-pick kinda problem
        """

        n = len(nums)
        total_sum = 0

        for i in nums:
            total_sum += i

        if total_sum % 2 == 1:
            return False
        
        find_sum = total_sum // 2

        dp = {}

        def util(curr, curr_sum):
            if curr >= n:
                return False

            if curr_sum + nums[curr] == find_sum:
                return True
            
            if (curr, curr_sum) in dp:
                return dp[(curr, curr_sum)]

            # not pick:
            not_pick = util(curr + 1, curr_sum)

            # pick:
            pick = util(curr + 1, curr_sum + nums[curr])

            dp[(curr, curr_sum)] = pick | not_pick

            return dp[(curr, curr_sum)]
            
        return util(0, 0)