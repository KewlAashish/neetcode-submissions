class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        """

        max_heap = []
        freq = {}

        for ch in tasks:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        for task, frequency in freq.items():
            heapq.heappush(max_heap, [-1*frequency, task])

        queue = deque() # time_to_insert_to_heap, frequency, task
        t = 1

        while max_heap or queue:
            task = None
            if max_heap:
                task = heapq.heappop(max_heap)
            if task:
                task_freq, task_ch = -1*task[0], task[1]
                task_freq -= 1

                if task_freq > 0:
                    queue.append([t + n, task_freq, task_ch])

            while queue and queue[0][0] == t:
                node = queue.popleft()
                heapq.heappush(max_heap, [-1*node[1], node[2]])

            t += 1

        return t - 1