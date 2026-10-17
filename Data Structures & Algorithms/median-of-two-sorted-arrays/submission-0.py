class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left_size = (m + n + 1) // 2

        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = left_size - i

            L1 = nums1[i - 1] if i > 0 else float("-inf")
            R1 = nums1[i] if i < m else float("inf")

            L2 = nums2[j - 1] if j > 0 else float("-inf")
            R2 = nums2[j] if j < n else float("inf")

            if L1 <= R2 and L2 <= R1:
                if (m + n) % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                else:
                    return max(L1, L2)
            elif L1 > R2:
                high = i - 1
            else:
                low = i + 1
                

        return -1










