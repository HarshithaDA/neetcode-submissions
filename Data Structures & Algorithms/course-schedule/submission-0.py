class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # map each course to prereq list
        preMap= {i:[] for i in range(numCourses)}
        for cr,pre in prerequisites:
            preMap[cr].append(pre)

        visit= set()

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True

            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            preMap[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True