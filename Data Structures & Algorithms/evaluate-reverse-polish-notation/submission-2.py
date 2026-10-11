class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '/', '*'}

        st = []
        ans = 0

        for i in tokens:
            if i in operators:
                n1 = st.pop()
                n2 = st.pop()
                resultant = 0
                if i == "+":
                    resultant = n2 + n1
                elif i == "-":
                    resultant = n2 - n1
                elif i == "*":
                    resultant = n2 * n1
                else:
                    resultant = int(n2 / n1)

                st.append(resultant)
                continue

            st.append(int(i))

        return st[-1]