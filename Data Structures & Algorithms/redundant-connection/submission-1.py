class Solution:
    
    def initiate(self, n):
        self.parent = list(range(n + 1))
        self.size = [1]*(n + 1)

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        
        if root_p == root_q:
            return False

        if self.size[root_p] < self.size[root_q]:
            root_p, root_q = root_q, root_p

        # Attach smaller component to larger
        self.parent[root_q] = root_p
        self.size[root_p] += self.size[root_q]

        return True

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 1
        
        for edge in edges:
            u = edge[0]
            v = edge[1]

            n = max(n, max(u, v))

        self.initiate(n)

        for edge in edges:
            u = edge[0]
            v = edge[1]

            if self.union(u, v):
                continue
            else:
                return edge

        return []

        


