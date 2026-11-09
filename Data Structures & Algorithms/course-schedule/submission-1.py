
class Solution:

    def dfs(self, node, graph, visiting, completed):

        if node in visiting:
            return False  # Cycle detected

        if node in completed:
            return True  # Already verified

        visiting.add(node)

        for child in graph[node]:
            if not self.dfs(child, graph, visiting, completed):
                return False

        visiting.remove(node)
        completed.add(node)

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        visiting = set()
        completed = set()

        for course in range(numCourses):
            if not self.dfs(course, graph, visiting, completed):
                return False

        return True
