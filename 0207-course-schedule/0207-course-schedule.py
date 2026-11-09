class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:      # cycle detected!
                return False
            if preMap[crs] == []:    # no prerequisites, can finish
                return True

            visitSet.add(crs)        # mark as "currently visiting"
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)     # done visiting this path
            preMap[crs] = []         # mark as fully checked (optimization)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True