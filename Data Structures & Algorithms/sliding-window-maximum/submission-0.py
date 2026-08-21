class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # indices
        l = r = 0

        while r<len(nums):
            # while q is not empty and while the top value (rightmost) in queue is less than the value we are inserting 
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            # if left value is out of bounds, remove left value from window
            if l> q[0]:
                q.popleft()

            if (r+1) >= k:
                # append the maximum ie the left most value of queue
                output.append(nums[q[0]])
                l+=1
            r+=1

        return output
            

