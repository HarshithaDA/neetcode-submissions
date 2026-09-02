class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # each character can only appear in one partition

        # hashmap for every character and its lastindex occurance
        # char, lastindex
        # end ptr so we can keep track of end of partition
        # size var so we can keep track of size of current partition
        # when size equals end - we have finished current partition
        # set size back to 0 and add to output

        # char -> lastindex
        hashmap = {} 
        for i,c in enumerate(s):
            hashmap[c] = i

        output = []
        size, end = 0,0
        for i, c in enumerate(s):
            # increment size by 1 every time we see a character
            size+=1
            # update end if lastindex is greater than current end
            end = max(end, hashmap[c])

            if i==end:
                output.append(size)
                size=0

        return output




         
