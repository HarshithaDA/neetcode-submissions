class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+len(nums2)
        half = total //2
        A, B = nums1, nums2

        # we only need to run binary search on one of them 
        if len(B)<len(A):
            A, B = B, A

        l, r = 0, len(A)-1
        while True:
            i = (l+r)//2 # middle index for A
            j = half - i -2 # middle index for B

            Aleft = A[i] if i>=0 else float("-infinity")
            Aright = A[i+1] if (i+1)<len(A) else float("infinity")

            Bleft = B[j] if j>=0 else float("-infinity")
            Bright = B[j+1] if (j+1)<len(B) else float("infinity")

            if Aleft <=Bright and Bleft<=Aright:
                # left partitions are correct
                # if theres an odd number of elements in total
                if total % 2:
                    return min(Aright, Bright)
                # if even length
                return (max(Aleft, Bleft) + min(Aright, Bright)) /2

            elif Aleft>Bright:
                # reduce size of left partition from A
                r=i-1
            else:
                l=i+1



