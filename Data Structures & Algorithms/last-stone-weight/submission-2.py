class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in stones:
            heapq.heappush(heap, -1*i)
        
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            result = abs(second - first)

            if result > 0:
                heapq.heappush(heap, -1*result)

        return 0 if not heap else -1*heap[0]