class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_start = 0
        r_end = len(matrix) - 1
        row_ind = -1

        while r_start <= r_end:
            r_mid = (r_start + r_end) // 2

            r_mid_start = matrix[r_mid][0]
            r_mid_end = matrix[r_mid][-1]

            if r_mid_start <= target and target <= r_mid_end:
                row_ind = r_mid
                break
            elif target <= r_mid_start:
                r_end = r_mid - 1
            else:
                r_start = r_mid + 1

        if row_ind == -1:
            return False

        target_range = matrix[row_ind]

        l = 0
        r = len(target_range) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == target_range[mid]:
                return True
            elif target < target_range[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False

