class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes=0
        lastused=s[0].lower()
        for i in range(len(s)-1):
                if s[i].lower() != s[i+1].lower():
                    changes+=1
        return changes  