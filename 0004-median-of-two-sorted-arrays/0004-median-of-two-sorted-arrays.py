class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2

        result = sorted(self.nums1+self.nums2)
        n = len(result)

        if n%2 == 0:
            median = (float(result[n // 2 - 1]) + result[n // 2]) / 2
        else:
            median = (float(result[n//2]))
        
        return median

solution = Solution()
nums1 = [1,3]; nums2 = [2]
add = solution.findMedianSortedArrays(nums1,nums2)
print(add)
        