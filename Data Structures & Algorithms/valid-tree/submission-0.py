class Solution:

    def dfs(self, node, graph, visited):

        visited.add(node)

        for child in graph[node]:
            if child in visited:
                continue

            self.dfs(child, graph, visited)

        return

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Each node can be reached from any other node in the graph - A dfs from any nodes randomly and if visited == n then I think we can reach any node
        Total edges shouldn't exceed n - 1 count
        """

        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]

            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        self.dfs(0, graph, visited)

        return len(visited) == n