class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        lowest_price=0
        if len(prices)>0:
            lowest_price=prices[0]
        else:
            return 0

        for p in prices:
            if p<lowest_price:
                lowest_price=p
            if p-lowest_price>max_profit:
                max_profit=p-lowest_price
        
        return max_profit