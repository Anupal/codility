class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """

        [[3,1],[3,2],[1,0],[1,4],[0,4]]
        3 ----> 1 ---> 0 -.
        '--->2  |         |
                '----> 4 <'
        """
        adjMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites: adjMap[course].append(prereq)

        ans, visited, cycle = [], set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            
            for prereq in adjMap[course]:
                if not dfs(prereq): return False

            ans.append(course)
            cycle.remove(course)
            visited.add(course)
            
            return True
        
        for course in adjMap:
            if not dfs(course): return []

        return ans