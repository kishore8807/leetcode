class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub=tu=0
        while sub<len(s) and tu<len(t):
            if s[sub]==t[tu]:
                sub+=1
            tu+=1
        return sub==len(s)