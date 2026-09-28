class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, l,m,r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            # j for left subarray starting
            # k for right subarray starting
            i, j, k = l,0,0

            while j<len(left) and k<len(right):
                # whichever has smaller value insert into input array
                if left[j]<=right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
               
                i+=1

            # once one of the subarrays have run out,
            # add the rest of the values of the other subarray
            while j<len(left):
                arr[i] = left[j]
                j+=1
                i+=1

            while k<len(right):
                arr[i] = right[k]
                k+=1
                i+=1
            
    
        def mergesort(arr, l, r):
           # if size of array is 1 
            if l>=r:
                return arr

            # merge sort on left and right
            m =(l+r)//2
            mergesort(arr, l, m)
            mergesort(arr,m+1, r)

            merge(arr, l, m, r)
            return arr

        return mergesort(nums, 0, len(nums)-1)
