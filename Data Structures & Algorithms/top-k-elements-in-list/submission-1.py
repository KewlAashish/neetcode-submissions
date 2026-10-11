class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_elements = Counter(nums)

        heap = []
        for element, freq in count_elements.items():
            heapq.heappush(heap, [freq, element])
        
            if len(heap) > k:
                heapq.heappop(heap)

        result = [i for j, i in heap]

        return result