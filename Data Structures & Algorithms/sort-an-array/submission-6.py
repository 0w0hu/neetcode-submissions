class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, l, m, r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            idx, li, ri = l, 0, 0
            while li < len(left) and ri < len(right):
                if left[li] < right[ri]:
                    arr[idx] = left[li]
                    li += 1
                else:
                    arr[idx] = right[ri]
                    ri += 1
                idx += 1
            
            while li < len(left):
                arr[idx] = left[li]
                li += 1
                idx += 1
            
            while ri < len(right):
                arr[idx] = right[ri]
                ri += 1
                idx += 1

            return arr

        def mergesort(arr, l, r):
            if l == r:
                return arr
            
            m = (l+r)//2
            mergesort(arr,l,m)
            mergesort(arr,m+1,r)
            merge(arr,l,m,r)
            return arr

        mergesort(nums, 0, len(nums))
        return nums