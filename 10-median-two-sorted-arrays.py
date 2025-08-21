import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[il3 nt]
        :rtype: float
        """
        
        nums3 = nums1 +nums2
        print(nums3)
        for i in range(len(nums3)):
            for j in range(0, len(nums3)-i-1):
                if nums3[j] > nums3[j+1]:
                    nums3[j+1], nums3[j] = nums3[j] , nums3[j+1]
        n = len(nums3)
        if n % 2 == 1:
            # If odd, return the middle element
            return int(nums3[n // 2])
        else:
            # If even, return the average of the two middle elements
            return int(nums3[n // 2 - 1] + nums3[n // 2]) / 2.0
        
            
        
sol = Solution()
print(sol.findMedianSortedArrays([1,3],[2]))
