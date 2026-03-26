class Solution(object):
    def findMaxAverage(self, nums, k):
        s=sum(nums[:k])
        m=s
        for i in range(k,len(nums)):
            s=s-nums[i-k]+nums[i]
            if s >m:
                m=s
        return m /float(k)