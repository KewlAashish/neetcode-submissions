class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        nodes_heap = []

        for time in times:
            u = time[0]
            v = time[1]
            t = time[2]

            graph[u].append((v, t))

        distance = {i: float("inf") for i in range(1, n + 1)}
        distance[k] = 0

        heapq.heappush(nodes_heap, (0, k))

        while nodes_heap:
            d, node = heapq.heappop(nodes_heap)

            if d > distance[node]:
                continue

            for child, w in graph[node]:
                new_dist = d + w
                if new_dist < distance[child]:
                    distance[child] = new_dist
                    heapq.heappush(nodes_heap, (new_dist, child))


        ans = max(distance.values())

        return -1 if ans == float("inf") else ans