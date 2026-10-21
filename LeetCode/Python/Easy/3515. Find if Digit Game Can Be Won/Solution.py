class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singledigit,doubledigit=0,0
        for i in nums:
            if i<10:
                singledigit+=i
            else:
                doubledigit+=i
        return singledigit!=doubledigit