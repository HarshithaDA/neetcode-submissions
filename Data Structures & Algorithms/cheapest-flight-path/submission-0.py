class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford algorithm - shortest path + atmost k stops
        # k+1 layers of bfs 
        # set current node to 0 and others to inf
        # check each edge - if new min path found replace in temp arry - get rid of inf and put min path 
        # replace everythingin temp array then at the end put in prices array
        
        prices=[float("inf")]*n
        prices[src] = 0

        for i in range(k+1):
            temp = prices.copy()
            # go thru every flight
            # source, destination, price
            for s, d, p in flights :
                # price is inf at this source node -cannot be reached
                if prices[s]==float("inf"):
                    continue
                # we found new shortest paht to destination node
                if prices[s] + p < temp[d]:
                    temp[d]= prices[s]+p
            
            prices=temp
        return -1 if prices[dst]==float("inf") else prices[dst]