#Time Complexity : O(V + E) where V is numCourses and E is len(prerequisites)
# Space Complexity : O(V + E)
# Did this code successfully run on Leetcode : Yes
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        graph = {}
        for pr in prerequisites:
            indegrees[pr[0]] += 1
            if pr[1] not in graph:
                graph[pr[1]] = []
            graph[pr[1]].append(pr[0])
        
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        if not q:
            return False
        
        count = len(q)
        if count == numCourses:
            return True
        
        while q:
            curr = q.popleft()
            dependencies = graph.get(curr)
            if dependencies:
                for dep in dependencies:
                    indegrees[dep] -= 1
                    if indegrees[dep] == 0:
                        q.append(dep)
                        count += 1
                        if count == numCourses:
                            return True
        
        return False
