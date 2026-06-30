class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = len(nums1)-1
        print(last)
        m, n = m-1, n-1

        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                print("appending", nums1[m])
                nums1[last] = nums1[m]
                m -= 1
            else:
                print("appending", nums2[n])
                nums1[last] = nums2[n]
                n -= 1
            last -= 1
        print(nums1, last, m, n)
        
        while m >= 0:
            nums1[last] = nums1[m]
            m -= 1
            last -= 1
        
        while n >= 0:
            nums1[last] = nums2[n]
            n -= 1
            last -= 1
        