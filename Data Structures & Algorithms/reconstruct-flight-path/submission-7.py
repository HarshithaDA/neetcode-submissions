class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's Algorithm is more efficient for Eulerian Paths
        adj = collections.defaultdict(list)

        # Sort in reverse lexical order to pop from the end (O(1) operation)
        tickets.sort(reverse=True)

        for src, dst in tickets:
            adj[src].append(dst)

        res = []

        def dfs(src):
            # Standard Hierholzer's approach: exhaust all edges for a node
            while adj[src]:
                neig = adj[src].pop()
                dfs(neig)
            res.append(src)

        dfs("JFK")
        return res[::-1]