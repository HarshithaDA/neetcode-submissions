class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        premap = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            premap[crs].append(pre)

        # a course has 3 possible states:
        # visited: crs has been added to output so we are never visiting this again
        # visiting: crs not added to output but added to cycle - green path
        # unvisited: crs not added to output or cycle 

        output = []
        visit = set() # current node already visited
        cycle = set() # current node along path

        def dfs(crs):
            # there is a loop/cycle so topological sort is not possible return []
            if crs in cycle:
                return False

            # do not need to visit a course twice
            if crs in visit:
                return True

            # add the course to the cycle
            cycle.add(crs)

            # get all prereqs of this crs and run dfs
            for pre in premap[crs]:
                if not dfs(pre): return False

            # remove crs from out cycle cuz its no longer along current path
            cycle.remove(crs)
            # add to visit node has been visited
            visit.add(crs)
            # add to output since we went thru all prereqs
            output.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs): return []
        return output