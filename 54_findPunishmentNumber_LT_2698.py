class Solution(object):
    def punishmentNumber(self, n):

        def can_partition(num,target): #helper function
            s = str(num) #convert number into string for effecting splitting

            def dfs(index,current_sum):
                if index == len(s): #when all elements are checked
                    return current_sum == target

                #trying partition in all possible ways
                for j in range(index +1 , len(s) +1):
                    part = int(s[index:j])
                    if dfs(j,current_sum + part):
                        return True
                return False
            return dfs(0,0)

        total = 0
        for i in range(1, n +1):
            square = i * i
            if can_partition(square,i):
                total += square
        return total
