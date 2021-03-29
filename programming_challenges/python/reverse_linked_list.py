#Leetcode 206
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #check if head is empty or is the only value
        if (head == None or head.next == None):
            return head
        
        #initialize pointers
        p = head.next
        q = p.next
        
        #start reversing the linked-list
        #set head point to null
        head.next = None
        
        #while not reached the end of the linked list...
        while(q != None):
            #moving pointer from right to left
            p.next = head

            #moving all three pointers to the right
            head = p #set p as the new head
            p = q #set q as the new p
            q = q.next #set q.next as the new q
        
        #when arrived at end of linked list,
        #move the last pointer from right to left.
        p.next = head
        #return resulting linked list
        return p
