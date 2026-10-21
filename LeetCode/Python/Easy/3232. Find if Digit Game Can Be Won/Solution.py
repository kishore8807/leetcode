class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        t,tt=0,0
        for i in nums:
            if i<10:
                t+=i
            else:
                tt+=i
        return t!=tt