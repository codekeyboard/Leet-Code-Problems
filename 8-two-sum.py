class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # if nums[i] + nums[j]:
                if nums[i] + nums[j] == target:
                    return [i,j]

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([1,2,3,4],3))