class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        
        count2 = {}
        for c in s2[:len(s1)]:
            count2[c] = count2.get(c, 0) + 1
        
        l, r = 0, len(s1)
        
        while r < len(s2):
            if count1 == count2:
                return True
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]
            l += 1
            r += 1
        
        if count1 == count2:
            return True
        
        return False