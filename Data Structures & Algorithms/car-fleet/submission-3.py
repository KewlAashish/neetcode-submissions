class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        n = len(position)

        for ind in range(n):
            st.append([position[ind], speed[ind]])
        
        st.sort()

        fleet = []

        for car in st:
            car_time = (target - car[0]) / car[1]

            while fleet and car_time >= fleet[-1]:
                    fleet.pop()
                
            fleet.append(car_time)
        
        return len(fleet)