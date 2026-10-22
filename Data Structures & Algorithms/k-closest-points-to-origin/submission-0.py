class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        n = len(points)

        for i in range(n):
            dist = (points[i][0]**2 + points[i][1]**2) ** 0.5
            if len(heap) == k:
                heapq.heappushpop(heap, [-1*dist, points[i][0], points[i][1]])
            else:
                heapq.heappush(heap, [-1*dist, points[i][0], points[i][1]])

        result = []

        while heap:
            node = heapq.heappop(heap)
            result.append([node[1], node[2]])
            
        return result
        

