class Solution:

    def utils(self, visited, combination, result, nums):
        if len(combination) == len(nums):
            result.append(combination.copy())
            return 

        for i in nums:
            if i in visited:
                continue

            visited.add(i)
            combination.append(i)

            self.utils(visited, combination, result, nums)

            visited.remove(i)
            combination.pop()
            
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