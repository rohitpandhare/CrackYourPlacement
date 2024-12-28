class Solution(object):
    def validPalindrome(self, s):
    #convert the string into list
        norm = list(s)
        #reverse the list
        rev = norm[::-1]
        
      #if the reverse and norm is same - its palindrome
        if rev == norm:
            return True
            
        for i in range(len(norm)):
            #check when its not -- palindrome -- and likely to become
            if norm[i] != rev[i]:
                # by not selecting the error part -- just skip that -- and make a new word from norm and rev
                t1 = norm[:i] + norm[i+1:]
                t2 = rev[:i] + rev[i+1:]

              #compare the new word and their reverses with itself with OR with t1 and t2
                if t1 == t1[::-1] or t2 == t2[::-1]:
                    return True
                else:
                #else return false
                    return False
                  #simply break the loop
                break
  
