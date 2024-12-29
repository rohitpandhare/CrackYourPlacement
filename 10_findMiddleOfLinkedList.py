# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
      # we will make 2 pointers and keep them at start of the LL
        slow, fast = head, head
        #run the while loop when fast and fast.next( next element to fast) is not none -- means it has not reached the END
        while fast is not None and fast.next is not None:
            slow = slow.next #slow moves by one pointer and reach MID of LL
            fast = fast.next.next #fast moves by 2 pointer and reach last of LL
        return slow # return the mid of LL

    
