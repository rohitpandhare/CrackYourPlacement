class Solution(object):
    def mincostTickets(self,days, costs):
        travel_days = set(days) #convert days array into list -- to make it unique
        last_day = days[-1] #get the last element of days array
        dp = [0] * (last_day + 1) #multiply the 0th list by no. of days +1

        for day in range(1, last_day + 1): #day 1 to days+1
            if day not in travel_days: #when days is not present in i/p list eg. days[1,5] then 2,3,4 are not present
                dp[day] = dp[day - 1] # we will simply copy our previous day cost of use 
            else: # take min of days cost by using Dynamic programming
                dp[day] = min(
                    dp[max(0, day - 1)] + costs[0],  # 1-day pass
                    dp[max(0, day - 7)] + costs[1],  # 7-day pass
                    dp[max(0, day - 30)] + costs[2]  # 30-day pass
                )
        return dp[last_day] #will return the min cost 


            
