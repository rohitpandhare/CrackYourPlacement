#see the basic principle of stock market is BUy at low and sell at high
class Solution(object):
    def maxProfit(self, prices):
      # see start the first element as left and the next element as right -- and use these variable as pointers for the comparison purpose
        left,right  = 0 ,1 
      #just for instance keep the max profit as - 0
        max_profit = 0

        #when right is not reached the end
        while right < len(prices):
          # when the buy is low( left) and selling ( right) is high -- or big
            if prices[left] < prices[right]:
              # so simply max - min profit
                profit = prices[right] -  prices[left]
              # select the max profit
                max_profit = max(max_profit,profit)
            else:
              # or when the left is more than right -- means the buy is high and sell is loww-- move to the right's position -- means we are getting some low buying power
                left = right
            #outside the else part- update the -- right -- while the but(left) is slowing checking and moving
            right += 1
        #outside the while loop in function we will return the maximum profit
        return max_profit

        
