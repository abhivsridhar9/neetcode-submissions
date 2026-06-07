class Solution:
    def isPalindrome(self, s: str) -> bool:
        L,R=0,len(s)-1

        while L<R:
            # 1. Skip non-alphanumeric from the left
            while L < R and not s[L].isalnum():
                L += 1
            # 2. Skip non-alphanumeric from the right
            while L < R and not s[R].isalnum():
                R -= 1
                
            if s[L].lower()!=s[R].lower():
                return False

            L +=1
            R -=1
    

        return True
