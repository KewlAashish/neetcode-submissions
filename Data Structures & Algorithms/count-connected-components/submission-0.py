class Solution:

    def dfs(self, node, visited, graph):
        visited.add(node)

        for child in graph[node]:
            if child in visited:
                continue
            
            self.dfs(child, visited, graph)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]

            graph[u].append(v)
            graph[v].append(u)

        count = 0
        visited = set()
        
        for node in range(n):
            if node in visited:
                continue

            count += 1

            self.dfs(node, visited, graph)

        return count