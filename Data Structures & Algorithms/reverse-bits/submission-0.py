class Solution:
    def reverseBits(self, n: int) -> int:
        s=0
        
        for i in range(32):
            s+=(n&1)*(2**(31-i))
            n=n>>1

        return s