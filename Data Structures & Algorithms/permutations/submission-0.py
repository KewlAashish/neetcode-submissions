class Solution:

    def utils(self, visited, combination, result, nums):
        if len(combination) == len(nums):
            result.append(combination)
            return 

        for i in nums:
            if i in visited:
                continue

            visited.add(i)
            self.utils(visited, combination + [i], result, nums)
            visited.remove(i)
            
        return


    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Bro feels like we need to pick an index i, loop over the others, select them and mark as visited
        Add it to the combination once and get them skipped in future iterations
        """

        permutations = []

        visited = set()
        self.utils(visited, [], permutations, nums)

        return permutations