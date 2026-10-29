class MedianFinder:

    def __init__(self):
        self.left_half = [] # max heap
        self.right_half = [] # min heap

    def addNum(self, num: int) -> None:
        if len(self.left_half) == 0:
            heapq.heappush(self.left_half, -num)
            return

        if len(self.left_half) == len(self.right_half):
            if self.right_half[0] < num:
                removed_num = heapq.heappop(self.right_half)
                heapq.heappush(self.left_half, -removed_num)
                heapq.heappush(self.right_half, num)
            else:
                heapq.heappush(self.left_half, -num)

        else:
            if -self.left_half[0] > num:
                removed_num = -heapq.heappop(self.left_half)
                heapq.heappush(self.right_half, removed_num)
                heapq.heappush(self.left_half, -num)
            else:
                heapq.heappush(self.right_half, num)

        return


    def findMedian(self) -> float:
        if len(self.left_half) == 0:
            return -1

        if len(self.left_half) == len(self.right_half):
            return (-self.left_half[0] + self.right_half[0]) / 2
        else:
            return -self.left_half[0]
        