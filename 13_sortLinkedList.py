# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a = []  #intializing an array
        current = head #a pointer
        while current is not None: #will work while current is not reach end -- 
            a.append(current.val) #append the array with LL elements
            current = current.next #like we do i++, update the pointer
        
        a.sort() #sort the array

        current = head #AGAIN synch the pointer with Head 
      '''
        for i in range(len(a)): # loop of sorting LL
            current.val = a[i]#copy the values
            current = current.next # i++
        '''
         for i in a: # loop of sorting LL
            current.val = i #copy the values
            current = current.next # i++

        return head #return LL
        
