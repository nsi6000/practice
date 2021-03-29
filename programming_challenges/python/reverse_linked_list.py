#Leetcode 206
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative solution
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

# Recursive solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)
    
    def reverse(self, head: ListNode, new_head: ListNode) -> ListNode:
        if (head == None):
            return new_head

        #defines second pointer as next of head
        n = head.next
        #moving pointer from right to left
        head.next = new_head
        #defines new_head as head (moves to right)
        new_head = head
        #defines head as next (moves to right)
        head = n
        return self.reverse(head, new_head)
