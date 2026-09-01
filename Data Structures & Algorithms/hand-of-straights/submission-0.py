class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # check min value and start a group with that value
        # count number of cards with each value with hashmap 
        # hashmap - value -> count
        # size of input array has to be divisible by groupsize
        # pop from minheap, check hashmap decrement count 
        # if we pop thats not the minimum -> return false

        if len(hand) % groupSize:
            return False

        # hashmap value->count
        count = {}
        for n in hand:
            count[n] = 1+count.get(n,0)

        # creating minheap 
        # distinct values
        minheap = list(count.keys())
        heapq.heapify(minheap)

        # till not empty, pop min value
        while minheap:
            first = minheap[0]

            for i in range(first, first+groupSize):
                # if value not in hashmap return false
                if i not in count:
                    return False

                # if value available, decrement by 1
                count[i] -= 1
                # if value at 0, pop from minheap
                # if we pop from minheap thats not the minimum-F
                if count[i] == 0:
                    if i!= minheap[0]:
                        return False
                    
                    # else pop
                    heapq.heappop(minheap)

        return True





