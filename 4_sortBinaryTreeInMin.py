# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minimumOperations(self, root):
        q = deque([root]) #intialize the queue for traversal
        swap = 0 #intialize counter for swaps

        def function(res):
            n = 0
            t = [x for x in res] #values for input paramete 'res' is being copied to t
            t.sort() #and simply sort them
            maps = {} #dictionary to keep track for hash value- hash map --

            for i in range(len(res)):
                maps[res[i]] = i #copy the original hash values for tree into the map{}
            
            for i in range(len(res)):
                if res[i] != t[i]: #if the value of the element in array is not at its correct position then we will check and swap it to the correct one
                    n += 1
                    temp = maps[t[i]]
                    maps[res[i]] = temp
                    res[temp] = res[i]
            return n

        while q: #to perform level order traversal-- loop continue untill queue is EMPTY
            n = len(q)  #count the node at current level
            res = [] 
            for i in range(n): # for the collection of res values
                node = q.popleft() #pop
                res.append(node.val) #push/append into res

                if node.left:
                    q.append(node.left) #append left to q

                if node.right:
                    q.append(node.right) #append right to q
            
            swap += function (res) # the adds the swap counts
        
        return swap # return the required swaps
