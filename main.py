class Solution:
    def firstUniqChar(self, s: str) -> int:
        si=Counter(s)
        for i,v in si.items():
            if v==1:
               return s.index(i)

        return -1