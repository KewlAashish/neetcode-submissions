class Solution:

    def dfs(self, node, target, visited, graph):
        if node == target:
            return True

        visited.add(node)

        for child in graph[node]:
            if child in visited:
                continue

            if self.dfs(child, target, visited, graph):
                return True

        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:

            visited = set()

            if self.dfs(u, v, visited, graph):
                return [u, v]

            graph[u].append(v)
            graph[v].append(u)

        return []