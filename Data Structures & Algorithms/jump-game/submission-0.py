class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # keep moving goal post from right end to left end
        goal = len(nums) - 1

        for i in range(len(nums)-1,-1,-1):
            # nums[i] is the jump length
            # if our jump from where we are can reach the goal
            # move the goal post position to i (left)
            if i+nums[i] >= goal:
                goal = i

        # when we reach the end - either 2 things will be true
        # if goal =0 -> from position 0 we can reach goal
        # if goal >0 -> not able to reach end of input list

        return True if goal == 0 else False

