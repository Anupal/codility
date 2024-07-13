class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """

        [[0,1],[0,2],[1,3],[1,4],[3,4]]
        0 ----> 1 ---> 3 -.
        '--->2  |         |
                '----> 4 <'
        """
        # create a map to store adjacencies (course: [prereqs])
        adjMap = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            adjMap[course].append(prereq)

        visited = set()

        def dfs(course):
            # already visited in this dfs
            if course in visited:
                return False
            # all prereqs visited -> empty list
            if not adjMap[course]:
                return True

            # recursively visit all prereqs
            visited.add(course)
            for prereq in adjMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            adjMap[course] = []
            return True

        # iterate through all courses in case graph is disconnected
        for course in adjMap:
            if not dfs(course):
                return False
        return True
