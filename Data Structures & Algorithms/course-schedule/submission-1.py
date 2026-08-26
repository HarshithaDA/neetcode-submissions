class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # map each course to prereq list
        preMap= {i:[] for i in range(numCourses)}
        # append prereqs to list
        for cr,pre in prerequisites:
            preMap[cr].append(pre)

        visit= set()

        def dfs(crs):
            # if already in visit set, there is a loop so course cannot be completed so return false
            if crs in visit:
                return False
                # no outward edges, no prereqs so we can complete it
            if preMap[crs] == []:
                return True

            visit.add(crs)
            # loop thru prereqs and run dfs on it
            for pre in preMap[crs]:
                # if dfs returns false we return false
                if not dfs(pre): return False
            # can be completed if dfs returns true so remove from visit set
            visit.remove(crs)
            # if course can be completed next time return true immediately - how do we achieve this we just set the prereqs to empty to return true
            preMap[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True