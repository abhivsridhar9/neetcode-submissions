class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        char_tracker=dict()

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s in char_tracker:
                char_tracker[char_s]+=1
            else:
                char_tracker[char_s]=1

            if char_t in char_tracker:
                char_tracker[char_t]-=1
            else:
                char_tracker[char_t]=-1
        
        for val in char_tracker.values():
            if val!=0:
                return False
        
        return True