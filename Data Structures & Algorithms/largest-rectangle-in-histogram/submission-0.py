class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        ans = 0
        n = len(heights)

        for i in range(n + 1):
            curr = heights[i] if i < n else 0

            while st and heights[st[-1]] > curr:
                mid = st.pop()
                left_boundary = -1 if not st else st[-1]
                ans = max(ans, heights[mid]*(i - left_boundary - 1))

            if i < n:
                st.append(i)
        
        return ans