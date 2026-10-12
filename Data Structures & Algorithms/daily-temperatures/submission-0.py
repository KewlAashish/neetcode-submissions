class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*(n)
        st = []

        for r in range(n):
            while st and temperatures[st[-1]] < temperatures[r]:
                older_day = st[-1]
                st.pop()
                result[older_day] = r - older_day

            st.append(r)

        return result