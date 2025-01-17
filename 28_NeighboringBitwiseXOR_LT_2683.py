class Solution(object):
    def doesValidArrayExist(self, derived):    
        #intialize 2 pointers 
        first = 0 
        last = 0
        #for - 101 -- for create the 1th term --- then we need two opposite numbers 0 1 and 1 
        for n in derived: #iterating through derived 
            if n: #if an element exits there
                last = ~last #reverse the number

        return first == last #if last first and last are same -- then there exists an ORIGINAL
