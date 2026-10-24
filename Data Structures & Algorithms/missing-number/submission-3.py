class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dict={}
        for i in range(0,len(nums)+1):
            dict[i]=1
        for j in dict.keys():
            if j not in nums:
                return j
                



        