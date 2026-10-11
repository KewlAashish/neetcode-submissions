class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        n = len(height)
        water = 0

        for i, h in enumerate(height):
            while st and h > height[st[-1]]:
                top = st.pop()

                if not st:
                    break

                width = i - st[-1] - 1
                hm = min(h, height[st[-1]]) - height[top]

                water += width*hm
            
            st.append(i)

        return water