class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for edge in prerequisites:  
            u = edge[1]
            v = edge[0]

            graph[u].append(v)
            indegree[v] += 1

        bfs = deque()

        for node in range(numCourses):
            if indegree[node] == 0:
                bfs.append(node)

        order = []
        completed = 0

        while bfs:
            node = bfs.popleft()
            order.append(node)
            completed += 1

            for next_course in graph[node]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    bfs.append(next_course)

        return order if completed == numCourses else []